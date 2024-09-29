'''Write a Python program build Decision Tree Classifier using Scikit-learn 
package for diabetes data set (download database from 
https://www.kaggle.com/uciml/pima-indians-diabetes-database) 
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 1: Load the dataset
def load_dataset(filepath):
    data = pd.read_csv("D:/Data Mining/Ass3/Set1/diabetes.csv")
    print("Dataset loaded successfully!")
    return data

# Step 2: Preprocess the data (if needed)
def preprocess_data(data):
    # Check for missing values and handle them if necessary
    print("\nMissing values in each column:")
    print(data.isnull().sum())

    # In this dataset, there are no missing values in the original dataset,
    # but you can implement handling of missing values if needed.

    return data

# Step 3: Split the dataset into training and testing sets
def split_dataset(data, target_column, test_size=0.2):
    X = data.drop(columns=[target_column])  # Features (excluding target column)
    y = data[target_column]  # Target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    print("\nDataset split into training and testing sets.")
    print(f"Training set size: {X_train.shape[0]} rows")
    print(f"Testing set size: {X_test.shape[0]} rows")

    return X_train, X_test, y_train, y_test

# Step 4: Build and train the Decision Tree Classifier
def train_decision_tree(X_train, y_train):
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)
    print("\nDecision Tree Classifier trained successfully!")
    return clf

# Step 5: Evaluate the model
def evaluate_model(clf, X_test, y_test):
    y_pred = clf.predict(X_test)

    print("\nAccuracy Score:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Main function to run the entire process
def main(filepath, target_column):
    # Load dataset
    data = load_dataset(filepath)

    # Preprocess the data
    data = preprocess_data(data)

    # Split the dataset
    X_train, X_test, y_train, y_test = split_dataset(data, target_column)

    # Train the Decision Tree Classifier
    clf = train_decision_tree(X_train, y_train)

    # Evaluate the model
    evaluate_model(clf, X_test, y_test)

# Path to the dataset
filepath = 'diabetes.csv'  # Update with your dataset path if needed

# The target column we want to predict
target_column = 'Outcome'  # This is the column representing diabetes status

# Run the main function
main(filepath, target_column)
