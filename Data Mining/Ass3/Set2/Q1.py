'''Consider following dataset 
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','S
unny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy'] 
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mi
ld','Mild','Hot','Mild'] 
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Y
es','No']. Use Naïve Bayes algorithm to predict[ 0:Overcast, 2:Mild] 
tuple belongs to which class whether to play the sports or not. 
'''

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

# Step 1: Define the dataset
weather = ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy']
temp = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild']
play = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']

# Step 2: Encode categorical data into numerical values
# Create label encoders for weather and temperature
le_weather = LabelEncoder()
le_temp = LabelEncoder()
le_play = LabelEncoder()

# Convert weather, temp, and play into numerical values
weather_encoded = le_weather.fit_transform(weather)  # Encode weather: Sunny=2, Overcast=0, Rainy=1
temp_encoded = le_temp.fit_transform(temp)  # Encode temp: Hot=1, Mild=2, Cool=0
play_encoded = le_play.fit_transform(play)  # Encode play: No=0, Yes=1

# Step 3: Combine weather and temp to create the feature set
features = np.array(list(zip(weather_encoded, temp_encoded)))  # Combine weather and temp into feature pairs

# Step 4: Train the Naive Bayes model
model = GaussianNB()
model.fit(features, play_encoded)  # Train the model on features (weather, temp) and labels (play or not)

# Step 5: Make the prediction for the tuple [0:Overcast, 2:Mild]
prediction = model.predict([[0, 2]])  # [0:Overcast, 2:Mild]

# Step 6: Decode the prediction back to the original class label
predicted_play = le_play.inverse_transform(prediction)  # Convert numeric prediction back to original label

# Output the prediction
print(f"The tuple [Overcast, Mild] belongs to the class: {predicted_play[0]}")
