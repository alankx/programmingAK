
setwd("C:/Users/staffgs29/Downloads")
weather_data <- read.csv('hw1_data.csv', header=TRUE)
plot(weather_data$Ozone, weather_data$Temp)
summary(weather_data)
cor(weather_data$Wind, weather_data$Temp)
plot(weather_data$Wind, weather_data$Temp)

wind_temp_model <- lm(Temp ~ Wind, data=weather_data)
abline(wind_temp_model)

summary(wind_temp_model)
pairs(weather_data)
cor(weather_data)