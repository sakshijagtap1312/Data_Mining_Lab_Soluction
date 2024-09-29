#2. Write a python program to splitting the dataset into training and testing set. 

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_target = pd.Series(iris.target, name='target')

# Display the original dataset
print("Original Dataset (First 5 Rows):\n", iris_data.head())

# Splitting the dataset into features (X) and target (y)
X = iris_data  # Features
y = iris_target  # Target variable

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the resulting sets
print("\nShape of Training Set (X_train):", X_train.shape)
print("Shape of Testing Set (X_test):", X_test.shape)
print("Shape of Training Labels (y_train):", y_train.shape)
print("Shape of Testing Labels (y_test):", y_test.shape)

# Optional: Save the split datasets to CSV files
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)

print("\nTraining and testing datasets saved as 'X_train.csv', 'X_test.csv', 'y_train.csv', and 'y_test.csv'.")
