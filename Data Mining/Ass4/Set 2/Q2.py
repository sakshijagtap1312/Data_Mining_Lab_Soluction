'''Write a Python program for Apriori Algorithm using ARM. And Print the Rule, 
Support, Confidence and Lift. 
- (Set Min_Support = 0.0040, Min_Confidence=0.2, Min_Lift=3, 
Min_Length=2) 
Note: Download dataset from following link : 
(https://www.kaggle.com/irfanasrullah/groceries)'''

# Import necessary libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Load the dataset
url = "D:/Data Mining/Ass4/Set 2/Groceries_dataset.csv"
groceries_data = pd.read_csv(url)

# Step 2: Preprocess the data into a transactional format
# Convert the dataset into a list of transactions
basket = groceries_data.groupby(['Member_number', 'itemDescription'])['itemDescription'].count().unstack().reset_index().fillna(0).set_index('Member_number')

# Convert the values to 1 (purchased) and 0 (not purchased)
basket = basket.applymap(lambda x: 1 if x > 0 else 0)

# Step 3: Apply the Apriori algorithm
frequent_itemsets = apriori(basket, min_support=0.0040, use_colnames=True)

# Step 4: Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=3)

# Filter rules based on minimum confidence
rules = rules[(rules['confidence'] >= 0.2) & (rules['lift'] >= 3) & (rules['antecedent_len'] >= 2)]

# Step 5: Print the results
print("Rules with Support, Confidence, and Lift:")
for index, row in rules.iterrows():
    print(f"Rule: {set(row['antecedents'])} -> {set(row['consequents'])}")
    print(f"Support: {row['support']:.4f}, Confidence: {row['confidence']:.4f}, Lift: {row['lift']:.4f}\n")
