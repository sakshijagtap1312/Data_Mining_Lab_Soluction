#Write a python program the Categorical values in numeric format for a given dataset. 

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset (Replace with your actual file path or URL)
url = "D:/Data Mining/Ass2/Set_1/timeseries.csv"
data = pd.read_csv(url)

# Display the original dataset
print("Original Dataset:\n", data.head())

# Function to convert categorical values to numeric
def convert_categorical_to_numeric(data):
    # Select categorical columns
    categorical_cols = data.select_dtypes(include=['object']).columns
    
    print("\nCategorical Columns:", list(categorical_cols))

    # Convert using Label Encoding for simplicity (For each categorical column)
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le

    print("\nDataset after converting categorical columns to numeric:\n", data.head())
    return data, label_encoders

# Convert categorical values to numeric
numeric_data, encoders = convert_categorical_to_numeric(data)

# Save the transformed dataset as a new CSV file
numeric_data.to_csv('numeric_dataset.csv', index=False)
print("\nNumeric dataset saved as 'numeric_dataset.csv'.")
