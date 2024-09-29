''' Write a python programme to implement multiple linear regression model for stock 
market data frame as follows:  
Stock_Market = {'Year': 
[2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,20
 16,2016,2016,2016,2016,2016,2016,2016,2016,2016], 
'Month': [12, 11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1], 
'Interest_Rate': 
[2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.7
 5,1.75,1.75,1.75,1.75], 
'Unemployment_Rate': 
[5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6
 .2,6.1], 
'Stock_Index_Price': 
[1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,
 958,971,949,884,866,876,822,704,719] } 
And draw a graph of stock market price verses interest rate. 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Stock market data
Stock_Market = {
    'Year': [2017, 2017, 2017, 2017, 2017],
    'Month': [12, 11, 10, 9, 8],
    'Interest_Rate': [ 2.5, 2.5, 4.1,2.5, 2.5],
    'Unemployment_Rate': [5.3, 5.3, 5.3, 5.3, 5.4],
    'Stock_Index_Price': [1464, 1394, 1357, 1293, 1256]
}

# Check lengths
for key, value in Stock_Market.items():
    print(f"{key}: {len(value)}")


# Creating DataFrame
df = pd.DataFrame(Stock_Market)

# Defining features and target variable
X = df[['Interest_Rate', 'Unemployment_Rate']]  # Independent variables
y = df['Stock_Index_Price']  # Dependent variable

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and fitting the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting values
y_pred = model.predict(X_test)

# Plotting Stock Index Price vs. Interest Rate
plt.scatter(df['Interest_Rate'], df['Stock_Index_Price'], color='blue', label='Data Points')
plt.title('Stock Index Price vs Interest Rate')
plt.xlabel('Interest Rate')
plt.ylabel('Stock Index Price')
plt.grid()
plt.legend()
plt.show()
