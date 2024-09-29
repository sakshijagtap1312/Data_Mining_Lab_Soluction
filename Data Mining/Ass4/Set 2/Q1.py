'''Write a Python program to read “StudentsPerformance.csv” file. Solve following:
- To display the shape of dataset. 
- To display the top rows of the dataset with their columns. 
- To display the number of rows randomly. 
- To display the number of columns and names of the columns. 
Note: Download dataset from following link : 
(https://www.kaggle.com/spscientist/students-performance-inexams?select=StudentsPerformance.csv)'''

# Import necessary libraries
import pandas as pd

# Step 1: Load the dataset
url = "D:\Data Mining\Ass4\Set 2\StudentsPerformance.csv"
students_performance = pd.read_csv(url)

# Step 2: Display the shape of the dataset
print("Shape of dataset:", students_performance.shape)

# Step 3: Display the top rows of the dataset
print("\nTop rows of the dataset:\n", students_performance.head())

# Step 4: Display a random sample of rows from the dataset
print("\nRandom sample of rows:\n", students_performance.sample(n=5))

# Step 5: Display the number of columns and names of the columns
print("\nNumber of columns:", students_performance.shape[1])
print("Names of the columns:", students_performance.columns.tolist())
