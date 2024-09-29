#1. Write a python program to find all null values in a given data set and remove them. (Download dataset from github.com)

import pandas as pd

# Function to load the dataset from a URL
def load_dataset(url):
    # Load the dataset
    data = pd.read_csv(url)
    print("Dataset loaded successfully!")
    return data

# Function to check for and remove null values
def remove_null_values(data):
    # Checking for null values
    null_values = data.isnull().sum()
    print("\nNull values in the dataset:")
    print(null_values)

    # Remove rows with null values
    data_cleaned = data.dropna()

    print("\nDataset after removing null values:")
    print(f"Number of rows before cleaning: {len(data)}")
    print(f"Number of rows after cleaning: {len(data_cleaned)}")

    return data_cleaned

# URL to the CSV file (Replace with your actual file path or URL)
url = "D:/Data Mining/Ass2/Set_1/timeseries.csv"

# Load dataset from the URL
data = load_dataset(url)

# Remove null values
cleaned_data = remove_null_values(data)

# Save the cleaned dataset to a new CSV file
cleaned_data.to_csv('cleaned_dataset.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_dataset.csv'.")
