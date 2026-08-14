import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#Dataset Load
df=pd.read_csv("c:/Users/ADMIN/Downloads/train.csv.zip")
print(df)

print(df.head())
print(df.shape)
print(df.info())

#Missing values and duplicates

print("Missing values:")
print(df.isnull().sum())

print("Duplicate Rows:")
print(df.duplicated().sum())

#Average purchase value
average_purchase_value=df["Sales"].mean()
print("Avarage Purchase Value",average_purchase_value)



#add customer lifetme value
customer_lifetime_value=df.groupby("Customer Name")["Sales"].sum()
print(customer_lifetime_value.head())
#prepare the important columns
df["Order Date"]=pd.to_datetime(df["Order Date"],errors="coerce")
df["Sales"]=pd.to_numeric(df["Sales"],errors="coerce")
df["Customer Name"]=df["Customer Name"].astype(str)
print(df[["Order ID","Order Date","Customer Name","Sales"]].head())

#Create the reference date
refernce_date=df["Order Date"].max()+pd.Timedelta(days=1)
print("Reference Date:",refernce_date)

#Crate RFM features
rfm=df.groupby("Customer Name").agg({
     "Order Date":lambda x:
        (refernce_date-x.max()).days,"Order ID":"nunique",
        "Sales":"sum"
       
} )
    

rfm.columns=["Recency","Frequency","Monetary"]

print(rfm.head())

#RFM descriptive statastics
print(rfm.describe())


# heck the RFM distribuition
plt.figure(figsize=(8,5))
plt.hist(rfm["Recency"],bins=20)

plt.title("Recency Distribution")
plt.xlabel("Recency")
plt.ylabel("Number of customers")
plt.show()

#
plt.figure(figsize=(8,5))
plt.hist(rfm["Frequency"],bins=20)
plt.title("Frequency  Distribution")
plt.xlabel("Number of orders")
plt.ylabel("Number of customers")
plt.show()

#
plt.figure(figsize=(8,5))
plt.hist(rfm["Monetary"],bins=20)
plt.title("Monetary value Distribution")
plt.xlabel("Total sales")
plt.ylabel("Number of customers")
plt.show()

print("Missing values in RFM:")
print(rfm[["Recency","Frequency","Monetary"]].isnull().sum())

rfm=rfm.dropna(subset=["Recency","Frequency","Monetary"])

print("RFM shape after cleaning:")
print(rfm.shape)

print("\nRemaining missing values:")
print(rfm[["Recency","Frequency","Monetary"]].isnull().sum())
# Standard dt he RFM data 
scaler=StandardScaler()
rfm_scaled=scaler.fit_transform(rfm)
rfm_scaled=pd.DataFrame(rfm_scaled,columns=["Recency","Frequency","Monetary"],
                        index=rfm.index)
print(rfm_scaled.head())


#Elbow Method
inertia=[]
for k in range(2,11):
    kmeans=KMeans(n_clusters=k,random_state=42,n_init=10)
    kmeans.fit(rfm_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8,5))
plt.plot(range(2,11),inertia,marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.show()

#k means clustering
kmeans=KMeans(n_clusters=4,random_state=42,n_init=10)
rfm["Cluster"]=kmeans.fit_predict(rfm_scaled)
print(rfm.head())
cluster_count=rfm["Cluster"].value_counts().sort_index()
print(cluster_count)

plt.figure(figsize=(8,5))
cluster_count.plot(kind="bar")
plt.title("Number of customers in each cluster")
plt.xlabel("CLuster")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.show()

#Cluster profiling
cluster_profile=rfm.groupby("Cluster")[["Recency","Frequency","Monetary"]].mean().round(2)

print(cluster_profile)


# fist scatter plot
plt.figure(figsize=(8,5))
sns.scatterplot(data=rfm,x="Recency",y="Monetary",hue="Cluster")
plt.title("Customer Segment:Recency vs Monetary")
plt.xlabel("Recency")
plt.ylabel("Monetary value")
plt.show()

#Second scatter plot
plt.figure(figsize=(8,5))
sns.scatterplot(data=rfm,x="Frequency",y="Monetary",hue="Cluster")
plt.title("Customer Segment:Frequency vs Monetary")
plt.xlabel("Frequency")
plt.ylabel("Monetary value")
plt.show()

#Create final customerr segment table
final_profie=rfm.groupby("Cluster").agg({"Recency":"mean","Frequency":"mean","Monetary":"mean"}).round(2)

final_profie["Customer count"]=(rfm.groupby("Cluster").size())
print(final_profie)

#Result f RFM save
rfm.to_csv("c:/Users/ADMIN/Downloads/train_cluster_segment_rfm.csv.zip")
print("RFM customer segmentation file saved successfully!")
