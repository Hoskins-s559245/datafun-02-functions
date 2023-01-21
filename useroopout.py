"""
Student Name: Ash Hoskins, Student #S559245
Course: CSIS 44-609 - Data Analytics Fundamentals
Professor Denise Case
Domain: Geospatial data
Module 2: Assignment 1 Task 5.

This is a simulation of the Pybuddy program to provide information about various Volcano.
The program prompts the user for which volcano they would like to read about and 
utilizes class objects to display the information in a presentable way.

WARNING: This script utilizes Inheritence from user_math.py from Task 3. To satisfy import math requirement
The method haversine is imported to the script in order to calculate the great circle path. 
Data Reference from: https://volcano.si.edu/gvp_currenteruptions.cfm

Terminal Results:
PS C:\Users\Hoski\Desktop\NWMS\GIT\datafun-02-functions\datafun-02-functions> & C:/Users/Hoski/miniconda3/python.exe c:/Users/Hoski/Desktop/NWMS/GIT/datafun-02-functions/datafun-02-functions/useroop.py

Welcome to PyBuddy Volcano Information Tool

1.) Lascar

2.) Etna

3.) Ahyi

4.) Klyuchevskoy


Please enter Which Volcano You want to Learn About (1-5): 1

The Volcano named Lascar is located in Chile
The elevation at the summit of Lascar is 5592 meters above or below sea levels
The Last eruption of started on 2022-12-10 and ended on 2022-12-19
The Longtitude is: 23.37 South and the Latitude is: 67.73 West
The Great Circle Path from Lascar to NWMS University is 2999526.31 Meters

PS C:\Users\Hoski\Desktop\NWMS\GIT\datafun-02-functions\datafun-02-functions> & C:/Users/Hoski/miniconda3/python.exe c:/Users/Hoski/Desktop/NWMS/GIT/datafun-02-functions/datafun-02-functions/useroop.py

Welcome to PyBuddy Volcano Information Tool

1.) Lascar

2.) Etna

3.) Ahyi

4.) Klyuchevskoy


Please enter Which Volcano You want to Learn About (1-5): 2

The Volcano named Etna is located in Italy
The elevation at the summit of Etna is 3357 meters above or below sea levels
The Last eruption of started on 2022-11-27 and ended on 2022-12-19
The Longtitude is: 37.748 North and the Latitude is: 14.999 East
The Great Circle Path from Etna to NWMS University is 8882090.52 Meters

PS C:\Users\Hoski\Desktop\NWMS\GIT\datafun-02-functions\datafun-02-functions> & C:/Users/Hoski/miniconda3/python.exe c:/Users/Hoski/Desktop/NWMS/GIT/datafun-02-functions/datafun-02-functions/useroop.py

Welcome to PyBuddy Volcano Information Tool

1.) Lascar

2.) Etna

3.) Ahyi

4.) Klyuchevskoy

5.) Surprise me (Random Choice)
Please enter Which Volcano You want to Learn About (1-5): 3

The Volcano named Ahyi is located in United States
The elevation at the summit of Ahyi is -75 meters above or below sea levels
The Last eruption of started on 2022-11-18 and ended on 2022-12-19
The Longtitude is: 20.42 North and the Latitude is: 145.03 East
The Great Circle Path from Ahyi to NWMS University is 5610741.26 Meters
There exists a volcanic activity report for Ahyi, There were explosions have been detected on January 15th

PS C:\Users\Hoski\Desktop\NWMS\GIT\datafun-02-functions\datafun-02-functions> & C:/Users/Hoski/miniconda3/python.exe c:/Users/Hoski/Desktop/NWMS/GIT/datafun-02-functions/datafun-02-functions/useroop.py

Welcome to PyBuddy Volcano Information Tool

1.) Lascar

2.) Etna

3.) Ahyi

4.) Klyuchevskoy


Please enter Which Volcano You want to Learn About (1-5): 4

The Volcano named Klyuchevskoy is located in Russia
The elevation at the summit of Klyuchevskoy is 4754 meters above or below sea levels
The Last eruption of started on 2022-11-17 and ended on 2022-12-19
The Longtitude is: 56.056 North and the Latitude is: 160.642 East
The Great Circle Path from Klyuchevskoy to NWMS University is 7333050.32 Meters

PS C:\Users\Hoski\Desktop\NWMS\GIT\datafun-02-functions\datafun-02-functions> & C:/Users/Hoski/miniconda3/python.exe c:/Users/Hoski/Desktop/NWMS/GIT/datafun-02-functions/datafun-02-functions/useroop.py

Welcome to PyBuddy Volcano Information Tool

1.) Lascar

2.) Etna

3.) Ahyi

4.) Klyuchevskoy

5.) Surprise me (Random Choice)


Great Choice!

The Volcano named Lascar is located in Chile
The elevation at the summit of Lascar is 5592 meters above or below sea levels
The Last eruption of started on 2022-12-10 and ended on 2022-12-19
The Longtitude is: 23.37 South and the Latitude is: 67.73 West
The Great Circle Path from Lascar to NWMS University is 2999526.31 Meters

PS C:\Users\Hoski\Desktop\NWMS\GIT\datafun-02-functions\datafun-02-functions> & C:/Users/Hoski/miniconda3/python.exe c:/Users/Hoski/Desktop/NWMS/GIT/datafun-02-functions/datafun-02-functions/useroop.py

Welcome to PyBuddy Volcano Information Tool

1.) Lascar

2.) Etna

3.) Ahyi

4.) Klyuchevskoy

5.) Surprise me (Random Choice)

Please enter Which Volcano You want to Learn About (1-5): 5

Great Choice!

The Volcano named Lascar is located in Chile
The elevation at the summit of Lascar is 5592 meters above or below sea levels
The Last eruption of started on 2022-12-10 and ended on 2022-12-19
The Longtitude is: 23.37 South and the Latitude is: 67.73 West
The Great Circle Path from Lascar to NWMS University is 2999526.31 Meters

PS C:\Users\Hoski\Desktop\NWMS\GIT\datafun-02-functions\datafun-02-functions>
"""