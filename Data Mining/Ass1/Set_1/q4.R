'''4. Write a script in R to create a list of employees and perform the following:
a. Display names of employees in the list.
b. Add an employee at the end of the list.
c. Remove the third element of the list.'''

# Initial list of employees
employees <- list("John", "Alice", "Michael", "Sara", "David")

# a. Display names of employees in the list
cat("Names of Employees:\n")
print(employees)

# b. Add an employee at the end of the list
new_employee <- "Emma"
employees <- append(employees, new_employee)
cat("\nAfter adding a new employee (Emma):\n")
print(employees)

# c. Remove the third element of the list
employees <- employees[-3]
cat("\nAfter removing the third employee (Michael):\n")
print(employees)
