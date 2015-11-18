#!/bin/python3
"""
######################################################################
 + Script       : DataTypes.py
 + Purpose      : This is a Tutorial file which will cover all the basic data types that are in python.
                  Data Types covered :
                1. Int
                2. Char & String
                3. Float & Decimal
                4. Imaginary
 + Created on   : 18/11/2015
 + Version      : 1.0
 + Changes      : 
    --> 1.0 : Basic Data types are covered: int, char and string, float
######################################################################
"""

"""
TODO:
    1. Implement 
        + Decimal
        + Imaginary
"""
"""
Datatypes in python are stateless. Meaning, we dont have to specify a variable what is it going to store while decleration. 
Also a variable declared for one type of data can be assigned with other types with out any explicit typecasting.
"""

# ==============
# Python Imports
# ==============
import sys

#                       Integer
# ===================================================

# An Integer can be assigned to variable in the followinf way. there is no constraint or the maximum value that can be assigned to the integer.
# If the value in integer crosses the maxint, the variable will be automatically converted to the long.
# Memory for the variable will be automatically allocated based on the size of the value.
print("\n\n################### Integer ########################")

# Variable assignment
print("Creating a integer variable i with value of 10 ... ")
i = 10

# Printing the value and the type of the above variable.
print("Variable i is created and is of type {0} and holding the value of {1}".format(type(i), i))

# Now let us see the maximum value that can be stored in a python variable (while keeping it still as int)
print("The Maxmum value that an integer variable can hold is : {0}".format(sys.maxsize-1))

# Now lets store the value which is more than the above max value and see the type of the variable
i += sys.maxsize

# With python3, there is no long variable, so even if we cross the maxvalue, the variable typically belongs to the same int class
print("Variable i is created and is of type {0} and holding the value of {1}".format(type(i), i))

# We can also have negative numbers in a variable. Lets change the existing i value to negative and see the properties of the variable
i *= -1
print("Variable i is created and is of type {0} and holding the value of {1}".format(type(i), i))


#                         Char and String
# =====================================================
"""
There is no distinction between character and String in Python. A character is a string with only one element in it.
String is often considered as an immutable object in the python linguo, but here lets see in a data type perspective.
"""

print("\n\n################### Char and String #######################")

# A string or character can be decalre in the following way.
c = 'a' # A character declaration
s = 'This is a string' # A string declaration

# Note : There is not distinction between a single quote(') and a double quote (") in Python. But as per PEP-8 standard, we usually use a double quote

# Now lets us see how to print and to find the type of a string variable.
print("Variable c declared as a character holding the value '{0}' and is of type {1}".format(c, type(c)))
print("Variable s declared as a character holding the value '{0}' and is of type {1}".format(s, type(s)))

# Refer Datastructures to check all the string related operations.


#                 Float and Decimals
# ================================================

"""
There is a little tricky thing with respect to Floats and Decimals in Python.
Both are capable of holding the fractional values, but Decimal has more advantages over float.
"""

print("\n\n################### Floats and Decimals #######################")
# First lets see the implementation of float

# A float value can be declared like any other datatypes string or int etc.

f = 3.1415

# Now lets see how this float value could be printed and its type.
print("Variable f is been assigned with the value : {0} and is of type :{1}".format(f, type(f)))

# Now lets decalre a decimal variable.


