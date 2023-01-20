"""
Student Name: Ash Hoskins, Student #S559245
Course: CSIS 44-609 - Data Analytics Fundamentals
Professor Denise Case
Module 2 - Assignment 1 - Task 4

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics

# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# Descriptive: Averages and measures of central tendency
mean = statistics.mean(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)

# Descriptive: Measures of spread
var = statistics.variance(scores)
stdev = statistics.stdev(scores)
lowest = min(scores)
highest = max(scores)


# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
#Two lists x_dates are a series of dates in 2023 from January 1st to January 13th
#y_rain are the reported rain fall amounts for the St. Louis, Missouri on those dates
x_dates = [20220101,20220102, 20220103, 20220104, 20220105,20220106, 20220107, 20220108, 20220109, 202201010, 202201011, 20220112, 20220113]
y_rain = [.00, .16, .81, .00, .00, .00, .22, .18, .00, .05, .61, .00, .00]

#Linear Regression method utilizing the two lists
slope, intercept = statistics.linear_regression(x_dates, y_rain)

#Setting the next date static for predictive analysis. future_y formats to  float to present it.
future_x = 20220114
future_y = float(slope * future_x + intercept)

#Test statistical correlation between the two lists, Note rainfall probably needs alot more samples for higher xy corr
xx = statistics.correlation(x_dates, x_dates)
xy = statistics.correlation(x_dates, y_rain)


#Displays information to the user formatted and cleanly presented. 
#First Part is for the Descriptive Measures
print(f"The Mean of the Scores Report is: {mean:.2f},")
print(f"The Median of the Scores Report is: {median:.2f},")
print(f"The Mode of the Scores Report is: {mode:.2f},")
print(f"The variance of the Scores Report is: {var:.2f},")
print(f"The Standard Deviation of the Scores Report is: {stdev:.2f},")
print(f"The Lowest Value of the Scores Report is: {lowest:.2f},")
print(f"The Highest Value of the Scores Report is: {highest:.2f},")
print()
print()
#This is the test correlation between the two variables
print(f"The correlation between Dates amongst itself = {xx:.2f}")
print(f"The correlation between Dates and Rainfall = { xy:.2f}")
print()
#Prediction results from the two variables with the linear regression.
print(f"The future date of = {future_x:d},")
print(f"There is a prediction of this amount of rainfall { future_y:.2f}.")