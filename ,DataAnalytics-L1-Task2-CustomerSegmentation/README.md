# OIBSIP Data Analytics Level 1 Task 2
## Customer Segmentation Analysis

### Objective
Apply clustering techniques to segment customers based on their purchasing behaviour and identify distinct customer groups for targeted marketing strategies.

### Dataset
The project uses customer order data containing information such as:
- Order ID
- Order Date
- Customer Name
- Sales

### Analysis Performed
- Loaded and inspected the dataset
- Handled missing values
- Prepared customer-level data
- Performed RFM analysis
- Calculated Recency, Frequency, and Monetary values
- Standardized RFM features using StandardScaler
- Used the Elbow Method to determine the number of clusters
- Applied K-Means clustering
- Assigned customers to different clusters
- Calculated mean RFM values for each cluster
- Analyzed the number of customers in each cluster
- Visualized customer segments using scatter plots

### Visualizations
- Recency distribution
- Frequency distribution
- Monetary value distribution
- Elbow Method
- Number of customers in each cluster
- Customer Segment: Recency vs Monetary
- Customer Segment: Frequency vs Monetary

### Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- K-Means Clustering

### Customer Segmentation
The customers were divided into 4 clusters based on their RFM characteristics.

### Cluster Summary
The clusters were compared using:
- Average Recency
- Average Frequency
- Average Monetary Value
- Number of customers

### Business Insights
The customer segments can be used to create targeted marketing strategies such as:
- Rewarding high-value customers
- Re-engaging less recent customers
- Encouraging repeat purchases
- Providing personalized offers

### Conclusion
RFM analysis combined with K-Means clustering helped identify different customer groups based on purchasing behaviour. These segments can support targeted marketing and customer relationship strategies.
