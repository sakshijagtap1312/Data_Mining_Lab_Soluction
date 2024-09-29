#1. Write a R program to reverse a number and also calculate the sum of digits of that number
reverse_and_sum_digits <- function(number) {
  
 
  number_str <- as.character(number)
    reversed_str <- paste(rev(strsplit(number_str, NULL)[[1]]), collapse = "")
    reversed_number <- as.integer(reversed_str)
    digits <- as.numeric(unlist(strsplit(number_str, NULL)))
  sum_of_digits <- sum(digits)
    cat("Original number:", number, "\n")
  cat("Reversed number:", reversed_number, "\n")
  cat("Sum of digits:", sum_of_digits, "\n")
}

reverse_and_sum_digits(1234) 
