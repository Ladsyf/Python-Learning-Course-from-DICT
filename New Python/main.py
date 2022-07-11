# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#

#Python for beginners course

#
# Variable declaration
#
#
"""
character_job = "pirate"
character_ride = "ship"
character_souvenir = "gold"
character_pet = "parrot"

print("There was once a " + character_job + " who loved adventure.")
print("The " + character_job + " would take her " + character_ride + " to unknown places")
print("She brings home a lot of " + character_souvenir + ".")
print("Then she goes home to her pet " + character_job + ", Chuckles")
"""

#
# Functions
#
"""
def hello(name, lastname):
    fullname = name + " " + lastname
    print("Hello " + fullname + "!")

hello("almar","javier")

def print_message(name):
    print("Have a nice day " + name)
print_message("almar")
"""

#
#Input function
#
"""
name = input("Enter your name: ")
print("Hi " + name + "!")

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter 2nd number: "))
print("Your numbers are: ", num1, " and ",num2, "!")
"""
#
"""
def addnum(num1, num2):
    total = num1 + num2
    return(total)

num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

print("The sum is : ",addnum(num1, num2))
"""

#
# Data types and Conversions
#
"""
isRaining = True #boolean
name = "James" #string
age = 21 #integer
money = 500.34 #float

#data conversion
int(23.43)
float(23)
str(23.43)
#methods that separates strings into individual characters
tuple() #contained by parentheses
list() #contained by square brackets

print(tuple(name))
print(list(name))

#boolean statement
print(10 > 7)
#converting int to string
print(str(73911))
#converting string to tuple
print(tuple("Thank God it's Friday!"))
#converting int to float
print(float(4302))
#converting float to int
print(int(3299.35640))

"""
