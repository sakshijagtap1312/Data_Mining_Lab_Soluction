'''1. Write a python program to implement k-means algorithm to build prediction model 
(Use Credit Card Dataset CC GENERAL.csv Download from kaggle.com) 
'''
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Step 1: Load the dataset (download CC GENERAL.csv from Kaggle)
# Assuming the dataset is in the same directory
url = 'D:\Data Mining\Ass6\set 1\CC GENERAL.csv'
data = pd.read_csv(url)

# Step 2: Data Preprocessing
# Drop any columns with too many missing values
data = data.dropna()

# Drop the CUST_ID column as it's not useful for clustering
data = data.drop('CUST_ID', axis=1)

# Check for missing values
print(data.isnull().sum())

# Step 3: Standardize the features
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Step 4: Apply K-Means Clustering
# We will use 5 clusters for this example
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(data_scaled)

# Add the cluster labels to the original data
data['Cluster'] = kmeans.labels_

# Step 5: Visualize the clusters using PCA
# Since we have many features, we'll reduce the dimensions using PCA to 2 components
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

# Create a DataFrame with the PCA components and cluster labels
pca_df = pd.DataFrame(data_pca, columns=['PCA1', 'PCA2'])
pca_df['Cluster'] = data['Cluster']

# Step 6: Plot the clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', palette='Set1', data=pca_df, s=100)
plt.title('K-Means Clustering of Credit Card Data (2D PCA)')
plt.show()

# Step 7: Analyze the cluster centers
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_centers_df = pd.DataFrame(cluster_centers, columns=data.columns[:-1])
print("Cluster Centers (Original Scale):\n", cluster_centers_df)
