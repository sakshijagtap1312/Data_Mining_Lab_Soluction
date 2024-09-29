'''Write a programme in python to print the number of outliers. Generate 200 samples, 
from a normal distribution, cantered around the value 100, with a standard deviation 
of 5. '''
import numpy as np
import pandas as pd

# Generate 200 samples from a normal distribution
np.random.seed(42)  # For reproducibility
samples = np.random.normal(loc=100, scale=5, size=200)

# Create a DataFrame
data = pd.DataFrame(samples, columns=['Value'])

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = data['Value'].quantile(0.25)
Q3 = data['Value'].quantile(0.75)

# Calculate the IQR
IQR = Q3 - Q1

# Determine the bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = data[(data['Value'] < lower_bound) | (data['Value'] > upper_bound)]

# Print the number of outliers
print(f'Number of outliers: {len(outliers)}')
