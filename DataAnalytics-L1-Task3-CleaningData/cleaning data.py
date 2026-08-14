import pandas as pd
import numpy as np

df=pd.read_csv("c:/Users/ADMIN/Downloads/retail_store_sales.csv")
print(df)

print("Dataset Shape:")
print(df.shape)

print("\n First 5 Rows:")
print(df.head())

print("\n Colum names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# Misssing values and duplicates
print("nMissing Vales:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

#Fill misssing values

#Categorical column
df["Item"]=df["Item"].fillna(df["Item"].mode()[0])
df["Discount Applied"]=df["Discount Applied"].fillna(df["Discount Applied"].mode()[0])

# Numerical columns
df["Price Per Unit"]=df["Price Per Unit"].fillna(df["Price Per Unit"].median())

df["Quantity"]=df["Quantity"].fillna(df["Quantity"].median())

df["Total Spent"]=df["Total Spent"].fillna(df["Total Spent"].median())

print("Missng values after cleaning:")
print(df.isnull().sum())

#Coonvert TransactionDate to datetime
d=pd.to_datetime(df["Transaction Date"],errors="coerce",dayfirst=True)
date_text=df["Transaction Date"].astype(str).str.strip()

#standardize seperators
date_text=date_text.str.replace("/","-",regex=False)

#Start with empty date column
df["Transaction Date"]=pd.NaT

#YYYY-MM-DDformat
mask_day_first=date_text.str.match(r"^\d{4}-\d{1,2}-\d{1,2}$")

df.loc[mask_day_first,"Transaction Date"]=pd.to_datetime(date_text[mask_day_first],format="%Y-%m-%d",errors="coerce")

#YYYY-MM-DDformat
mask_day_first=date_text.str.match(r"^\d{1,2}-\d{1,2}-\d{4}$")

df.loc[mask_day_first,"Transaction Date"]=pd.to_datetime(date_text[mask_day_first],format="%d-%m-%Y",errors="coerce")

print("\nInvalid Dates:")
print(df["Transaction Date"].isnull().sum())

print("\nData Type:")
print(df["Transaction Date"].dtype)

#Checking cleaning Dataset
print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nFinal Data Types:")
print(df.dtypes)

#Check for incorrect numeric values
print("Numeric column summary")
print(df[["Price Per Unit","Quantity","Total Spent"]].describe())

print("\nNegative Values:")
print("Negative price:")
print((df["Price Per Unit"]<0).sum())

print("Negativee Quantity:")
print((df["Quantity"]<0).sum())

print("Neagtive Total Spent:")
print((df["Total Spent"]<0).sum())

#Check unique values before standardisation
text_columns=["Category","Item","Payment Method","Location"]
for col in text_columns:
    print("\n",col)
    print(df[col].dropna().unique())

#Standardise text vlaues
df["Item"]=df["Item"].str.strip().str.title()

df["Payment Method"]=df["Payment Method"].str.strip().str.title()

df["Location"]=df["Location"].str.strip().str.title()

print("Standardisation Completed:")
print("\nPyment Methods:")
print(df["Payment Method"].unique())

print("\nLocations:")
print(df["Location"].unique())

#Outlier Detection using IQR
numeric_columns=["Price Per Unit","Quantity","Total Spent"]

for col in numeric_columns:
    Q1=df[col].quantile(0.25)
    Q3=df[col].quantile(0.75)
    IQR=Q3-Q1

    lower_limit=Q1-1.5*IQR
    upper_limit=Q3+1.5*IQR
    outliers=df[(df[col]<lower_limit)|(df[col]>upper_limit)]

    print("\nColumn:",col)
    print("Lower Limit:",lower_limit)
    print("Upper Limit",upper_limit)
    print("Number of Outliers:",len(outliers))

#Cap outliers usingIQR
numeric_columns=["Price Per Unit","Quantity","Total Spent"]

for col in numeric_columns:
    Q1=df[col].quantile(0.25)
    Q3=df[col].quantile(0.75)
    IQR=Q3-Q1

    lower_limit=Q1-1.5*IQR
    upper_limit=Q3+1.5*IQR
    df[col]=df[col].clip(lower=lower_limit,upper=upper_limit)

print("Outliers have been capped using the IQR method.")

df["Transaction ID"]=df["Transaction ID"].astype(str)
df["Customer ID"]=df["Customer ID"].astype(str)
df["Price Per Unit"]=pd.to_numeric(df["Price Per Unit"],errors="coerce")
df["Quantity"]=pd.to_numeric(df["Quantity"],errors="coerce")
df["Total Spent"]=pd.to_numeric(df["Total Spent"],errors="coerce")
print(df.dtypes)

#Final data quality 

print("Final Dataset Shape:")
print(df.shape)

print("\nFinal Missing Vlaues:")
print(df.isnull().sum().sum())

print("\nFinal Duplicate Rows:")
print(df.duplicated().sum())

print("\nFinal Data Types:")
print(df.dtypes)

df.to_csv("c:/Users/ADMIN/Downloads/retail_store_sales_cleand.csv",index=False)
print("Cleaned dataseet saved succesfully!")

#Before vs after summary 
print("====BEFORE vs AFTER=====")
print("\nFinal Rows:",len(df))
print("Final Clumns:",len(df.columns))

print("\nTotal Missing Vlaues:",df.isnull().sum().sum())
print("Total Duplicated Rows:",df.duplicated().sum())

print("\nFinal Data Types:")
print(df.dtypes)

#Verify the cleaned file
cleaned_df=pd.read_csv("c:/Users/ADMIN/Downloads/retail_store_sales_cleand.csv")
print("Cleaned filre loaded successfully!")
print("Rows and Column :",cleaned_df.shape)
print("\nMissing Vlues:",cleaned_df.isnull().sum().sum())
print("Diplicated Rows:",cleaned_df.duplicated().sum())