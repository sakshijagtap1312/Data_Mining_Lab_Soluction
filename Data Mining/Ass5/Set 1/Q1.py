#Consider following observations/data. And apply simple linear regression and find
#out estimated coefficients b0 and b1.( use numpy package)
#x= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,11,13]
#y = ([1, 3, 2, 5, 7, 8, 8, 9, 10, 12,16, 18]

import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12, 16, 18])

n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x_squared = np.sum(x ** 2)

b1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
b0 = (sum_y - b1 * sum_x) / n

print(f"Estimated coefficients:")
print(f"b0 (intercept): {b0}")
print(f"b1 (slope): {b1}")
