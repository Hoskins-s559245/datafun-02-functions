"""
Student Name: Ash Hoskins, Student #S559245
Course: CSIS 44-609 - Data Analytics Fundamentals
Professor Denise Case
Module 2: Assignment 1 Task 3.

This script calculates the area of a lot, utilzies math libraries for comb and perm with
the given values in the assignment. The 3 custom functions 1.) converts longitude and latitude to radians
2.) Utilizes the haversine formula to calculate the great spherical distances between the loscar volcano and
Northwest Missouri State University Campus. 3.) Converts haversine results from meters to miles.

"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width # Corrected for Task 3, Step 6 (Part A)
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)
# Function to convert longitude and latitude Angles to radians
def DtoR(long, lat):
    try:
        lo = math.radians(long)
        la = math.radians(lat)
        return lo, la
    except Exception as ex:
        print(f"Error: {ex}")
        return None
# Haversine formula for calculating great-circle distance between two points on a sphere.
# Calculates the shortest distance over the Earth's Surface following a great-circle path.
def Haversine(long2, lat2) :
    try:
        r = round(63710000/10)
        nwmslong = 40.3520
        nwmslat = 94.8825
        
        theta1 = lat2 * math.pi/180
        theta2  = nwmslat * math.pi/180
        alphaphi = (lat2 - nwmslat) * math.pi/180
        alphalambda = (long2 - nwmslong) * math.pi/180

        a = math.sin(alphaphi/2) * math.sin(alphaphi/2) + math.cos(theta1) * math.cos(theta2) * math.sin(alphalambda/2) * math.sin(alphalambda/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        Distance = r * c
        return Distance   
    except Exception as ex:
        print(f"Error: {ex}")
        return None
#Simply converts meters to miles.       
def meterstomiles(meters) :
    try:
        miles = meters * .00062137
        return miles
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print()

    #Printing and calling functions within the domain for the Module assignment.
    print("The Location of the Lascar Volcano in Chile is: 23.37 degrees south,  67.73 degrees west")
    print("The Coordinates in radians is: ", DtoR(23.37,67.73))
    #Places haversine results into variable for miles converstion
    zx = round(Haversine(23.37, 67.73),)
    print("The Great Spherical Distance of The Lascar Volcano to NWMS University is: ",zx, " Meters or",round(meterstomiles(zx), 2), " Miles" )

    #Module 2, Task 3, Step 2 (Part B) - Calling method/function with values 6,2
    print("The Area of the Lot is: ", get_area_of_lot(6,2))