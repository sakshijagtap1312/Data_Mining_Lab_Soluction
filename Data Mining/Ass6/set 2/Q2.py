#Write a python program to implement hierarchical clustering algorithm. (Download 
#Wholesale customers data dataset from github.com). 
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Step 1: Load the dataset
url = "D:\Data Mining\Ass6\set 2\Wholesale customers data.csv"
data = pd.read_csv(url)

# Step 2: Data Preprocessing (optional: scale the data)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Step 3: Perform Hierarchical Clustering using AgglomerativeClustering
hierarchical_cluster = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels = hierarchical_cluster.fit_predict(data_scaled)

# Step 4: Create a DataFrame for easier analysis
data['Cluster'] = labels

# Step 5: Visualize the Dendrogram (using linkage for hierarchical clustering visualization)
linked = linkage(data_scaled, method='ward')

plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()

# Step 6: Plot the clustered data (optional, using first two features)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=data['Fresh'], y=data['Milk'], hue=data['Cluster'], palette='Set1', s=100)
plt.title("Hierarchical Clustering (Agglomerative) - Wholesale Customers Data")
plt.show()
