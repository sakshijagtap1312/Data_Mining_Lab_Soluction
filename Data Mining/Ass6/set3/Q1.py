''' Write a python program to implement Agglomerative clustering on a synthetic dataset. 
(use inbuilt Iris data set).'''

# Import necessary libraries
# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
import pandas as pd

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target  # True labels (just for comparison, not used in clustering)

# Step 2: Perform Agglomerative Clustering
# n_clusters = 3 because there are 3 species in the Iris dataset
agg_clustering = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
labels = agg_clustering.fit_predict(X)

# Step 3: Visualize the clusters using PCA (Principal Component Analysis)
# PCA for reducing to 2D for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Step 4: Create a DataFrame for easier plotting
df = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
df['Cluster'] = labels

# Step 5: Plot the clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', palette='Set1', s=100)
plt.title("Agglomerative Clustering on Iris Dataset (PCA projection)")
plt.show()
