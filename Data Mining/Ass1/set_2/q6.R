#6. Write a R program to perform the following:
#a. Display all the cars having mpg more than 20.
#b. Subset the data set by mpg column for values greater than 15.0
#c. Display all cars having four gears.
#(Use inbuilt data set mtcar) 

# Use the built-in mtcars dataset
data("mtcars")

# a. Display all cars having mpg more than 20
cat("Cars with mpg greater than 20:\n")
mpg_gt_20 <- subset(mtcars, mpg > 20)
print(mpg_gt_20)

# b. Subset the data set by mpg column for values greater than 15.0
cat("\nCars with mpg greater than 15.0:\n")
mpg_gt_15 <- subset(mtcars, mpg > 15)
print(mpg_gt_15)

# c. Display all cars having four gears
cat("\nCars with 4 gears:\n")
cars_with_four_gears <- subset(mtcars, gear == 4)
print(cars_with_four_gears)

