'''2. Write a python program to implement hierarchical Agglomerative clustering algorithm. 
(Download Customer.csv dataset from github.com).'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Step 1: Load the dataset
url = r"D:\Data Mining\Ass6\set 1\Mall_Customers.csv"  # Using raw string for path
data = pd.read_csv(url)

# Step 2: Preprocess the data (using 'Annual_Income_(k$)' and 'Spending_Score')
X = data[['Annual_Income_(k$)', 'Spending_Score']]

# Step 3: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Perform Hierarchical Agglomerative Clustering
agg_clustering = AgglomerativeClustering(n_clusters=5, linkage='ward')
labels = agg_clustering.fit_predict(X_scaled)

# Step 5: Add cluster labels to the original data
data['Cluster'] = labels

# Step 6: Visualize the Dendrogram
Z = linkage(X_scaled, method='ward')

plt.figure(figsize=(10, 7))
dendrogram(Z, truncate_mode='lastp', p=12, show_leaf_counts=False, leaf_rotation=90., leaf_font_size=12.)
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Cluster Size')
plt.ylabel('Distance')
plt.show()

# Step 7: Visualize the clusters using a scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Annual_Income_(k$)', y='Spending_Score', hue='Cluster', palette='Set1', data=data, s=100)
plt.title('Agglomerative Clustering on Customer Data')
plt.show()
