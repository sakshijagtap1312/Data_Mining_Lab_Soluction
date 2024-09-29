''''Write a Python program build Decision Tree Classifier for shows.csv from 
pandas and predict class label for show starring a 40 years old American 
comedian, with 10 years of experience, and a comedy ranking of 7? Create 
a csv file as shown in 
https://www.w3schools.com/python/python_ml_decision_tree.asp 
'''
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Step 1: Load the dataset (Fixing the file path issue)
data = pd.read_csv(r'D:\Data Mining\Ass3\Set1\shows.csv')  # Use raw string or double backslashes

# Step 2: Convert categorical data into numerical values
data['Nationality'] = data['Nationality'].map({'UK': 0, 'USA': 1, 'N': 2})
data['Go'] = data['Go'].map({'YES': 1, 'NO': 0})

# Step 3: Define features (X) and target (y)
X = data[['Age', 'Experience', 'Rank', 'Nationality']]  # Features
y = data['Go']  # Target label (Go or No Go)

# Step 4: Train the Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Step 5: Predict the class label for a 40-year-old American comedian with 10 years of experience and a comedy ranking of 7
# Fixing the feature names warning by passing a DataFrame for prediction
new_data = pd.DataFrame([[40, 10, 7, 1]], columns=['Age', 'Experience', 'Rank', 'Nationality'])
prediction = clf.predict(new_data)

# Step 6: Output the prediction
print("Prediction for the show: ", "Go" if prediction[0] == 1 else "No Go")
