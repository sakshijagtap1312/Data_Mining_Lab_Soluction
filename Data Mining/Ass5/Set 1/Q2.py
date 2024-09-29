#Consider following observations/data. And apply simple linear regression and find
#out estimated coefficients b1 and b1 Also analyse the performance of the model
#(Use sklearn package)
#x = np.array([1,2,3,4,5,6,7,8])
#y = np.array([7,14,15,18,19,21,26,23])

# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Data (x and y)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)  # Reshape to 2D array
y = np.array([7, 14, 15, 18, 19, 21, 26, 23])

# Step 1: Create a linear regression model
model = LinearRegression()

# Step 2: Fit the model
model.fit(x, y)

# Step 3: Get the coefficients (b0 and b1)
b0 = model.intercept_   # Intercept (b0)
b1 = model.coef_[0]     # Slope (b1)

print(f"Estimated coefficients: b0 = {b0}, b1 = {b1}")

# Step 4: Make predictions
y_pred = model.predict(x)

# Step 5: Evaluate the model performance
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Step 6: Visualize the regression line
plt.scatter(x, y, color='blue', label='Actual data')
plt.plot(x, y_pred, color='red', label='Fitted line')
plt.title('Simple Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


