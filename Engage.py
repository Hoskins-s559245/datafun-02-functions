"""
Student Name: Ash Hoskins, Student #S559245
Course: CSIS 44-609 - Data Analytics Fundamentals
Professor Denise Case
Module 2 - Discussion: Engage Practice with Pandas
"""
import pandas as pd

d1 = {'FirstSet': pd.Series([10, 11, 14, 20, 20, 20, 22, 24, 28, 31])}
d2 = {'SecondSet': pd.Series([2, 9, 13, 14, 20 , 20 , 24, 26, 32, 40])}

df = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

s1 = df.mean()
s2 = df2.mean()
s3 = df.median()
s4 = df2.median()
s5 = df.mode()
s6 = df2.mode()


print("The Mean of the two datasets is")
print(s1.to_string(index = False))
print(s2.to_string(index = False))
print("***************")
print("The Median of the two datasets is")
print(s3.to_string(index = False))
print(s4.to_string(index = False))
print("***************")
print("The mode of the two data sets is")
print(s5.to_string(index = False))
print (s6.to_string(index = False))
