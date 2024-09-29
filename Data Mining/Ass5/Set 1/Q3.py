#Consider the student data set It can be downloaded from: 
#https://drive.google.com/open?id=1oakZCv7g3mlmCSdv9J8kdSaqO5_6dIOw 
#Write a programme in python to apply simple linear regression and find out mean 
#absolute error, mean squared error and root mean squared error. 

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
url = 'https://drive.google.com/uc?id=1oakZCv7g3mlmCSdv9J8kdSaqO5_6dIOw'
dataset = pd.read_csv(url)
x = dataset[['Hours']].values
y = dataset['Scores'].values
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')
