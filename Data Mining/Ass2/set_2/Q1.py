#1. Write a python program to rescale the data between 0 and 1. (use inbuilt dataset)
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler

# Load inbuilt dataset (Iris dataset)
iris = load_iris()
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)

# Display original dataset
print("Original Dataset:\n", iris_data.head())

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Rescale data between 0 and 1
iris_data_scaled = scaler.fit_transform(iris_data)

# Convert scaled data back to a DataFrame
iris_data_scaled_df = pd.DataFrame(iris_data_scaled, columns=iris.feature_names)

# Display rescaled dataset
print("\nRescaled Dataset (Between 0 and 1):\n", iris_data_scaled_df.head())

# Save the rescaled data to a CSV file (optional)
iris_data_scaled_df.to_csv('iris_data_rescaled.csv', index=False)
print("\nRescaled dataset saved as 'iris_data_rescaled.csv'.")
