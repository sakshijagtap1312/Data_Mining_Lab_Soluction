#4. Write a R program to create a data frame using two given vectors and display the duplicate elements 
# Define two vectors
vector1 <- c(1, 2, 3, 4, 5, 2, 3)
vector2 <- c("apple", "banana", "cherry", "apple", "banana", "grape", "cherry")

# Create a data frame using the vectors
df <- data.frame(ID = vector1, Fruit = vector2)

# Display the data frame
cat("Original Data Frame:\n")
print(df)

# Find and display duplicate elements in both columns
duplicates_vector1 <- vector1[duplicated(vector1)]
duplicates_vector2 <- vector2[duplicated(vector2)]

cat("\nDuplicate elements in 'ID' column:\n")
print(unique(duplicates_vector1))

cat("\nDuplicate elements in 'Fruit' column:\n")
print(unique(duplicates_vector2))
