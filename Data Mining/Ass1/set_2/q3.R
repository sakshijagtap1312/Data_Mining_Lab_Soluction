#3. Write a R program to concatenate two given factors.

# Define two factors
factor1 <- factor(c("Apple", "Banana", "Cherry"))
factor2 <- factor(c("Orange", "Mango", "Grapes"))

# Convert factors to character type and concatenate
concatenated_factors <- factor(c(as.character(factor1), as.character(factor2)))

# Print the results
cat("Factor 1:\n")
print(factor1)

cat("\nFactor 2:\n")
print(factor2)

cat("\nConcatenated Factor:\n")
print(concatenated_factors)
