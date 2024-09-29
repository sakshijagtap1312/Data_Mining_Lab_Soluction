'''1) Write a Python Programme to read the dataset (“Iris.csv”). dataset download from 
(https://archive.ics.uci.edu/ml/datasets/iris) and apply Apriori algorithm. 
'''
# Import necessary libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Load the Iris dataset from a CSV file
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# Column names as per the dataset description
column_names = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Class']
iris_data = pd.read_csv(url, header=None, names=column_names)

# Step 2: Ensure all the relevant columns are converted to numeric data
iris_data['SepalLength'] = pd.to_numeric(iris_data['SepalLength'], errors='coerce')
iris_data['SepalWidth'] = pd.to_numeric(iris_data['SepalWidth'], errors='coerce')
iris_data['PetalLength'] = pd.to_numeric(iris_data['PetalLength'], errors='coerce')
iris_data['PetalWidth'] = pd.to_numeric(iris_data['PetalWidth'], errors='coerce')

# Step 3: Discretize continuous features into categorical bins (e.g., low, medium, high)
# We'll use pd.cut to create categories for each feature
iris_data['SepalLength'] = pd.cut(iris_data['SepalLength'], bins=3, labels=['Short', 'Medium', 'Long'])
iris_data['SepalWidth'] = pd.cut(iris_data['SepalWidth'], bins=3, labels=['Narrow', 'Medium', 'Wide'])
iris_data['PetalLength'] = pd.cut(iris_data['PetalLength'], bins=3, labels=['Short', 'Medium', 'Long'])
iris_data['PetalWidth'] = pd.cut(iris_data['PetalWidth'], bins=3, labels=['Narrow', 'Medium', 'Wide'])

# Step 4: One-hot encoding for the categorical features to create transactions
one_hot_encoded_data = pd.get_dummies(iris_data)

# Step 5: Apply the Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(one_hot_encoded_data, min_support=0.3, use_colnames=True)

# Step 6: Generate association rules from the frequent itemsets
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Output the frequent itemsets and association rules
print("Frequent Itemsets:\n", frequent_itemsets)
print("\nAssociation Rules:\n", rules)
