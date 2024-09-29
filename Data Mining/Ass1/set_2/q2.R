#2. Write a R program to calculate the sum of two matrices of given size. 
# Define two matrices
matrix1 <- matrix(c(1, 2, 3, 4, 5, 6), nrow = 2, ncol = 3)
matrix2 <- matrix(c(6, 5, 4, 3, 2, 1), nrow = 2, ncol = 3)

# Calculate the sum of the two matrices
matrix_sum <- matrix1 + matrix2

# Print the matrices and their sum
cat("Matrix 1:\n")
print(matrix1)

cat("\nMatrix 2:\n")
print(matrix2)

cat("\nSum of Matrix 1 and Matrix 2:\n")
print(matrix_sum)
