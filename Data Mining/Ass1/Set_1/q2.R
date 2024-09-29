# Define the function first
multiplication_table <- function(number, range) {
  cat("Multiplication Table for", number, ":\n")
  for (i in 1:range) {
    result <- number * i
    cat(number, "x", i, "=", result, "\n")
  }
}

# Now call the function after defining it
multiplication_table(5, 10)  # Example: multiplication table of 5 up to 10

