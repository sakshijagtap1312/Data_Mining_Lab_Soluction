#5. Write a R program to perform the following:
#a. Display all rows of the data set having weight greater than 120.
#b. Display all rows of data set in ascending order of weight.
 #(Use inbuilt data set woman) 

 # Use the built-in women dataset
data("women")

# a. Display all rows where weight is greater than 120
cat("Rows where weight is greater than 120:\n")
subset_weight_gt_120 <- subset(women, weight > 120)
print(subset_weight_gt_120)

# b. Display all rows in ascending order of weight
cat("\nData sorted in ascending order of weight:\n")
sorted_women <- women[order(women$weight), ]
print(sorted_women)
