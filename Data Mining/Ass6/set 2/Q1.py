#1. Write a python program to implement k-means algorithms on a synthetic dataset.
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Step 1: Create a synthetic dataset
# Generate 2D data points with 3 clusters
X, y = make_blobs(n_samples=300, centers=3, cluster_std=0.6, random_state=0)

# Step 2: Apply K-Means Clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Step 3: Visualize the clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

# Step 4: Plot the cluster centers
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.title('K-Means Clustering on Synthetic Data')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
