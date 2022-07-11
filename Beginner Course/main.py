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
#
# Classes
#
"""
class Customers:
    greeting = "Welcome to the coffee Palace!"

c_1 = Customers()

c_1.name = "Samirah"
c_1.beverage = "Iced caffe latte"
c_1.food = "Cinnamon roll"
c_1.total = 225

c_2 = Customers()

c_2.name = "Jerry"
c_2.beverage = "Caramel macchiato"
c_2.food = "Glazed doughnot"
c_2.total = 230

print(Customers.greeting)
print("What does Samirah want to drink? " + c_1.beverage)
print("What does Jerry want to eat? " + c_2.food)
"""

#
# Arithmetic operators and precedence
# addition (+); subtraction(-); multiplication(*); division(/)
# modulus(%); Exponentiation(**); Floor Division(//)
# Precedence: PEMDAS
"""
# Addition
print(600+35234)
# Subtraction
print(2-1)
# Multiplication
print(217*6)
# Division
print(4/2)
# Modulus
print(56329%982)
# Exponentiation - Exponent
print(34**5)
# Floor Division - eliminates remainder, returns whole number(rounded off)
print(67//12)
"""

#
# Comparison and Logical Operators
# Comparison/Relational:  ==; !=; >; <; >=; <=;
# Logical: and; or; not - reverses the result

"""sdsd"""

#
# if else elif
#

"""
if 3>2:
    print("3 is greater than 2")
elif 4<6:
    print("4 is less than 6")
else:
    print("Last option")
"""

#
# Loops and Iterations
# You can use continue or break
"""
for x in "guitar":
    print(x)

hobbies = ["Playing Guitar", "Singing", "Coding", "Cooking", "Playing Games"]

for x in hobbies:
    print(x)

# range
r = range(8)
for x in r:
    print(x)


#while loop
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("i is greater than or equal to 10")

#nested
colors = ["Purple", "Red", "Orange", "Yellow"]
things = ["Car", "Notebook", "Shirt", "Shoes"]

for x in colors:
    for y in things:
        print(x, y)

"""