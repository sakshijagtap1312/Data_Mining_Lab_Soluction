'''1. Write a R Program to perform the following:
a. Create a Scattered plot to compare wind speed and temperature.
b. Create a Scattered plot to show the relationship between ozone and wind values
by giving appropriate values to colour argument.
c. Create a Bar plot to show the ozone level for all the days having temperature > 70.
 (Use inbuilt dataset air quality) 
'''

# Load necessary library
library(ggplot2)

# Load the airquality dataset
data("airquality")

# 1a. Scatter plot to compare wind speed and temperature
ggplot(airquality, aes(x = Wind, y = Temp)) +
  geom_point(color = "blue") +
  labs(title = "Scatter Plot of Wind Speed vs Temperature", x = "Wind Speed", y = "Temperature")

# 1b. Scatter plot to show the relationship between ozone and wind values
ggplot(airquality, aes(x = Wind, y = Ozone)) +
  geom_point(aes(color = Ozone)) +
  labs(title = "Scatter Plot of Ozone vs Wind", x = "Wind Speed", y = "Ozone Levels") +
  scale_color_gradient(low = "yellow", high = "red", na.value = "grey")

# 1c. Bar plot to show ozone levels for all the days having temperature > 70
ggplot(subset(airquality, Temp > 70), aes(x = as.factor(Day), y = Ozone)) +
  geom_bar(stat = "identity", fill = "skyblue") +
  labs(title = "Ozone Levels for Days with Temperature > 70", x = "Day", y = "Ozone Levels") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))  # Rotate x-axis labels for better visibility
