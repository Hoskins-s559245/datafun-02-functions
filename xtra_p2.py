"""
Student Name: Ash Hoskins, Student #S559245
Course: CSIS 44-609 - Data Analytics Fundamentals
Professor Denise Case
Domain: Geospatial data
Module 2: Assignment 1 Task 7: Xtra.

This script utilizes the doctest library by testing the methods
with predefined arguments. The purpose of this assignment was to fix the functions
so they work properly with the doctest below and stress test the funciontality. 


Optional bonus. See course site for details.



>>> add_two(1,2)
3

>>> add_two("hello"," world")
'hello world'

>>> add_triangle_list( [3,4,5] )
12

>>> add_any(1,1,1,1,1,1,1,1)
8

>>> add_any_with_keywords(a=1,b=2)
3

>>> convert_ctof(0)
32.0

>>> convert_ctof(100)
212.0
"""

import doctest

# define some existing functions
def add_two(first, second):
    """Return the sum of any two arguments."""
    sum = first + second  # Sums two variables
    return sum


def add_triangle_list(list_triangle):
    """Return the sum of three numbers in a list."""
    sum = 0
    for value in list_triangle:
        sum += +value  # fixed to add the value to the sum
    return sum


def add_any(*args):
    """Return the sum of numbers, using built-in *args."""
    sum = 0
    for x in args:
        sum += +x  # Fixed to add X to the sum of the arguments
    return sum


def add_any_with_keywords(**kwargs):
    """Return the sum of numbers, using built-in keyword args, **kwargs."""
    sum = 0
    for value in kwargs.values():  # use values() - name doesn't matter
        sum += +value  # add the value of each key in the kwargs.
    return sum


# TODO: implment a new function to convert celsius to fahrenheit
# Use round as needed to make the test pass
# The name of the function is provided in the docstring above
# Converts Celcius to Fahrenheit
def convert_ctof(i):
    temp = (i * 1.8) + 32
    return temp


if __name__ == "__main__":
    doctest.testmod()