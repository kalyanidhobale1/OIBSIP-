# OIBSIP Data Analytics Level 1 Task 3
## Cleaning Data

### Objective
Clean and transform a messy retail store sales dataset into a clean and analysis-ready dataset while documenting the data cleaning decisions.

### Dataset
The project uses a retail store sales dataset containing customer, transaction, payment, location, date, and sales-related information.

### Data Cleaning Performed
- Inspected the dataset structure
- Checked for missing values
- Checked for duplicate records
- Checked and corrected date formats
- Identified invalid dates
- Standardized categorical values
- Standardized payment methods
- Standardized location values
- Checked numeric columns
- Performed numeric column summary
- Detected outliers using the IQR method
- Handled extreme values using IQR-based capping
- Corrected data types
- Performed a final data quality check

### Standardization
Payment Method values were standardized to:
- Digital Wallet
- Credit Card
- Cash

Location values were standardized to:
- Online
- In-store

### Data Quality Verification
The cleaned dataset was checked again for:
- Missing values
- Duplicate rows
- Invalid dates
- Incorrect data types

### Tools Used
- Python
- Pandas
- NumPy
- Jupyter Notebook

### Output
A cleaned version of the dataset was created and saved as:

`retail_store_sales_cleaned.csv`

### Conclusion
The messy retail sales dataset was successfully cleaned and transformed into an analysis-ready dataset. The cleaning process improved data consistency, corrected data types and formats, handled outliers, and prepared the dataset for further analysis.
