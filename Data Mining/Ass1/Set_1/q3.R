#3. Write a R program to sort a list of strings in ascending and descending order.
# Define a list of strings
string_list <- c("apple", "orange", "banana", "grape", "mango")

# Sort the list in ascending order
ascending_order <- sort(string_list)

# Sort the list in descending order
descending_order <- sort(string_list, decreasing = TRUE)

# Print the results
cat("Sorted list in Ascending Order:\n", ascending_order, "\n")
cat("Sorted list in Descending Order:\n", descending_order, "\n")
