'''2) Write a Python Programme to apply Apriori algorithm on Groceries dataset. 
Dataset can be downloaded from 
(https://github.com/amankharwal/Websitedata/blob/master/Groceries_dataset.csv) 
Also display support and confidence for each rule. 
'''

# Import necessary libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Import necessary libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Load the dataset from the provided URL
url = "D:\Data Mining\Ass4\Set 1\Groceries_dataset.csv"
groceries_data = pd.read_csv(url)

# Step 2: Preprocess the data into a transactional format
# We'll pivot the data so that each transaction has one row and items as columns
basket = pd.crosstab(groceries_data['Member_number'], groceries_data['itemDescription'])

# Step 3: Convert the basket data to 1s and 0s (binary) for the Apriori algorithm
# Any non-zero value in the crosstab should be converted to 1 (indicating item bought)
basket = basket.applymap(lambda x: 1 if x > 0 else 0)

# Step 4: Apply the Apriori algorithm
frequent_itemsets = apriori(basket, min_support=0.01, use_colnames=True)  # Support threshold of 1%

# Step 5: Generate association rules with support, confidence, and lift
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.2)

# Step 6: Display the frequent itemsets
print("Frequent Itemsets:\n", frequent_itemsets)

# Step 7: Display the association rules with support, confidence, and lift
print("\nAssociation Rules:\n", rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
