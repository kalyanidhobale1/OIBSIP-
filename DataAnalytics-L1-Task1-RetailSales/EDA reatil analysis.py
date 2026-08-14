import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

#Dataset load
data=pd.read_csv("C:/Users/ADMIN/Downloads/retail_sales_dataset.csv")
print(data)

#initial inspetion
df=pd.DataFrame(data)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.shape)
print(df.dtypes)
print(df.duplicated().sum())


#Descriptive statastics
print("Mean:")
print(df.mean(numeric_only=True))

print("\nMedian:")
print(df.median(numeric_only=True))

print("\nMode:")
print(df.mode(numeric_only=True).iloc[0])

print("\n Standard Deviation:")
print(df.std(numeric_only=True))



#convert date colum to datetime
df["Date"]=pd.to_datetime(df["Date"])

print(df["Date"].min())
print(df["Date"].max())


#Monthly sales Trend
df["Month"]=df["Date"].dt.to_period("M")

monthly_sales=df.groupby("Month")["Total Amount"].sum()

print(monthly_sales)

plt.figure(figsize=(12,5))
monthly_sales.plot(kind="line",marker="o")

plt.title("Monthly sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#Qurterly Sales Trend

df["Quarter"]=df["Date"].dt.to_period("Q")
Qurterly_sales=df.groupby("Quarter")["Total Amount"].sum()
plt.figure(figsize=(10,5))
Qurterly_sales.plot(kind="line",marker="o")

plt.title("quarterly sales Trend")
plt.xlabel("Quarter")
plt.ylabel("Total sales")
plt.grid(True)
plt.show()

# customer Age Groups
bins=[17,25,35,45,55,65]
labels=["18-25","26-35","36-45","46-55","56-65"]

df["Age Group"]=pd.cut(df["Age"], bins=bins, labels=labels)
age_group=df["Age Group"].value_counts().sort_index()

print(age_group)
plt.figure(figsize=(8,5))
age_group.plot(kind="bar")

plt.title("Customer Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.show()

# Gender Distribution
gender_count=df["Gender"].value_counts()

print(gender_count)

plt.figure(figsize=(7,5))
gender_count.plot(kind="bar")

plt.title("Customer Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number Of Customers")
plt.xticks(rotation=0)
plt.show()

#Quantity sold by product category
category_quantity=(df.groupby("Product Category")["Quantity"].sum().sort_values(ascending=False))
print(category_quantity)

plt.figure(figsize=(8,5))
category_quantity.plot(kind="bar")
plt.title("Quantity sold by product category")
plt.xlabel("Product category")
plt.ylabel("Quantity sold")
plt.xticks(rotation=0)
plt.show()

#Revenue by product category
category_revenue=(df.groupby("Product Category")["Total Amount"].sum().sort_values(ascending=False))
print(category_revenue)
plt.figure(figsize=(8,5))
category_revenue.plot(kind="bar")
plt.title("Revenue by product category")
plt.xlabel("Product Category")
plt.ylabel("Total revenue")
plt.xticks(rotation=0)
plt.show()

#corellation Heatmap
numeric_data=df.select_dtypes(include="number")
correlation=numeric_data.corr()

plt.figure(figsize=(10,6))
sns.heatmap(correlation,annot=True,cmap="coolwarm",fmt=".2f")

plt.title("Correlation Matrix")
plt.show()

#sales by gender

gender_sales=df.groupby("Gender")["Total Amount"].sum()
print(gender_sales)
plt.figure(figsize=(7,5))
gender_sales.plot(kind="bar")

plt.title("Total sales by gender")
plt.xlabel("Gender")
plt.ylabel("Total sales")
plt.xticks(rotation=0)
plt.show()
