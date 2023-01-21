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
"""
#Import of libraries and methods
import datetime
import random
from enum import Enum
from user_math import Haversine


class nomenclature(Enum):
    Lascar = 1
    Etna = 2
    Ahyi = 3
    Klyuchevskoy = 4

#Primary Class Identifier PyBuddy
class PyBuddy:
    def __init__(obj, name, country, elev, erupstart, eruptstop, long, dir1,  lat, dir2):
    #Built in method to assign properties to the obj object.
        obj.name = name
        obj.country = country
        obj.elev = elev
        obj.erupstart = erupstart
        obj.eruptstop = eruptstop
        obj.long = long
        obj.dir1 = dir1
        obj.lat = lat
        obj.dir2 = dir2
        obj.haversine = round(Haversine(long, lat),2)

    def __str__(obj):
    #Built in method to describe the properties loaded into the object
        s0 = f"The Volcano named {obj.name} is located in {obj.country}\n"
        s1 = f"The elevation at the summit of {obj.name} is {obj.elev} meters above or below sea levels\n"
        s2 = f"The Last eruption of started on {obj.erupstart} and ended on {obj.eruptstop}\n"
        s3 = f"The Longtitude is: {obj.long} {obj.dir1} and the Latitude is: {obj.lat} {obj.dir2}\n"
        s4 = f"The Great Circle Path from {obj.name} to NWMS University is {obj.haversine} Meters\n"
    
    #Ahyi has an active Weekly Volcanic Activity Report; modifies return value for that selection
        if obj.name == "Ahyi" :
            s5 = f"There exists a volcanic activity report for {obj.name}, There were explosions have been detected on January 15th\n"
            s = s0+s1+s2+s3+s4+s5
        else :
            s = s0+s1+s2+s3+s4
        return s

if __name__ == "__main__": 
#Creates a menu for the user to be able to select which volcano to learn about or a randomized option; returns integer.
    def showmenu():
        print("\nWelcome to PyBuddy Volcano Information Tool")
        print("\n1.) Lascar")
        print("\n2.) Etna")
        print("\n3.) Ahyi")
        print("\n4.) Klyuchevskoy")
        print("\n5.) Surprise me (Random Choice)")
        print()
        selection = int(input("Please enter Which Volcano You want to Learn About (1-5): "))
        return selection

    #Assigns integer from showmenu method
    data = showmenu()

    #If option 5 is chosen in the menu a random selection from the list is made
    if(data == 5):
        print()
        print("Great Choice!")
        z = random.choice([1,2,3,4])
    else:
        z = data
    #Whichever integer is chosen by the user, the volcano information is sent to Pybuddy and the __str_ property of the class 
    #is called and displayed.
    if(z == 1):
        print()
        Lascar = PyBuddy("Lascar", "Chile", 5592, datetime.date(2022, 12, 10), datetime.date(2022, 12, 19), 23.37, "South", 67.73, "West")
        print(Lascar.__str__())
    elif(z == 2):
        print()
        Etna = PyBuddy("Etna", "Italy", 3357, datetime.date(2022,11,27), datetime.date(2022, 12, 19), 37.748, "North", 14.999,"East")
        print(Etna.__str__())
    elif(z == 3):
        print()
        Ahyi = PyBuddy("Ahyi", "United States", -75, datetime.date(2022, 11, 18), datetime.date(2022, 12, 19), 20.42, "North", 145.03, "East")
        print(Ahyi.__str__())
    elif(z == 4):
        print()
        Klyuchevskoy = PyBuddy("Klyuchevskoy", "Russia", 4754, datetime.date(2022,11,17), datetime.date(2022, 12,19), 56.056, "North", 160.642, "East")
        print(Klyuchevskoy.__str__())