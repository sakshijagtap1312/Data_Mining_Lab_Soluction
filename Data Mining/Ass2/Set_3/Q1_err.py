''' Write a python program to implement complete data pre-processing in a given data 
set.(missing value, encoding categorical value, Splitting the dataset into the training 
and test sets and feature scaling.(Download dataset from github.com). '''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.impute import SimpleImputer

# Step 1: Load dataset from a local file
def load_dataset(filepath):
    data = pd.read_csv(filepath)
    print("Dataset loaded successfully!")
    print("\nColumns in the dataset:", data.columns.tolist())  # Print column names
    return data

# ... [rest of the code remains unchanged]

# Main function to implement complete data preprocessing
def data_preprocessing_pipeline(filepath, target_column):
    # Load dataset
    data = load_dataset(filepath)

    # Handle missing values
    data = handle_missing_values(data)

    # Encode categorical values
    data, _ = encode_categorical_values(data)

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = split_dataset(data, target_column)

    # Feature scaling
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)

    print("\nPreprocessing completed.")
    return X_train_scaled, X_test_scaled, y_train, y_test

# Path to the dataset
filepath = 'Ass2/Set_1/timeseries.csv'

# Specify the target column name after checking the printed column names
target_column = 'your_actual_target_column'  # Replace with your actual target column

# Run the complete data preprocessing pipeline
X_train_scaled, X_test_scaled, y_train, y_test = data_preprocessing_pipeline(filepath, target_column)

# Optional: Save the preprocessed data to CSV files
pd.DataFrame(X_train_scaled).to_csv('X_train_scaled.csv', index=False)
pd.DataFrame(X_test_scaled).to_csv('X_test_scaled.csv', index=False)
pd.DataFrame(y_train).to_csv('y_train.csv', index=False)
pd.DataFrame(y_test).to_csv('y_test.csv', index=False)

print("\nPreprocessed datasets saved as 'X_train_scaled.csv', 'X_test_scaled.csv', 'y_train.csv', and 'y_test.csv'.")
