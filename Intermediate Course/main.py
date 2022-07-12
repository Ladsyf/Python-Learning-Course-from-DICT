# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

import functionfile
from functionfile import convertUSDtoPHP
from functionfile import convertPHPtoUSD
import random
import datetime

#
# Using INIT method
#
"""
class Guest:
    def __init__(self, name, age, number, interest):
        self.name = name
        self.age = age
        self.number = number
        self.interest = interest

guest1 = Guest("Juan", 21, "0213812", "Music")
guest2 = Guest("Marry", 20, "42323", "Programming")
guest3 = Guest("Joseph", 23, "02123432423812", "Gaming")

print(guest2.name + "' interest is: " + guest2.interest)
print(guest1.name + "' number is is: " + guest1.number)
print(guest3.name + "' age is:", guest2.age)
"""
"""
class Customers:
    greeting = "Welcome to the Coffee Palace!"
    def __init__(self, name, beverage, food, total):
        self.Name = name
        self.Beverage = beverage
        self.Food = food
        self.Total = total

c1 = Customers("Nate", "Espresso", "Food", 220)
c2 = Customers("Elaine","Strawberry Frappuccino", "Tuna Wrap", 270 )
c3 = Customers("Samirah", "Iced Caffe Latte", "Cinnamon Roll", 225)
c4 = Customers("Jerry","Caramel Macchiato", "Glazed Doughnut", 230)
c5 = Customers("Paz", "Iced Tea", "Blueberry Pancakes", 315)

print(Customers.greeting)
print(c2.Name + " will order " + c2.Beverage + " and " + c2.Food + " with the total of", c2.Total)
print(c4.Name + " will order " + c4.Beverage + " and " + c4.Food + " with the total of", c4.Total)
"""

#
# Inheritance/ Method overriding/ Super method
#
"""
class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display1(self):
        print("Name: " + self.name)
        print("Birthday: " + self.birthday)
        print("Age:", self.age)
        print("Favorite Food: " + self.favorite_food)
        print("Goal: " + self.goal)

class ClubOfficers (ClubMembers):
    def __init__(self, name, birthday, age, favorite_food, goal, position):
        self.position = position
        super().__init__(name, birthday, age, favorite_food, goal)

    def display2(self):
        super().display1()
        print("Position: " + self.position)

m_1 = ClubMembers("Tom", "January 16", 14, "Ice cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", 16, "Beef Stroganoff", "To be the world's greatest chef","Treasurer")

m_1.display1()
print("")
o_4.display2()

"""

#
# Dictionary
#
"""
flavors = ["vanilla", "chocolate", "strawberry", "cookies n' cream", "bubblegum"]
toppings = ["almonds", "banana slices", "chocolate syrup", "caramel syrup", "white chocolate chips"]

ice_cream = zip(flavors,toppings)
print("Using only zip(): ")
print(ice_cream)
ice_cream = dict(ice_cream)
print("Using dict(): ")
print(ice_cream)

ice_cream["chocolate"] = "blueberries"

ice_cream.update({"matcha": "pistachios", "ube": "mango slices"})
print(ice_cream)
"""

#
# Using Dictionaries
#
"""
groceries = {"chicken": 8, "apples": 6, "cucumbers": 3, "milkd": 2, "oranges": 4}

groceries.pop("oranges")

print(groceries)
print(groceries["chicken"])
print(groceries.get("chicken"))
print(groceries.items())
print(groceries.keys())
print(groceries.values())
"""

#
# Looping through the dictionary/nested dictionary
#
"""
hobbies = {"james": "singing", "joseph": "dancing", "john": "playing games"}

for key, value in hobbies.items():
    print(key + " likes to " + value)

#nested dictionary
batch = {1: {"matthew": 1.00, "mark": 2.25, "luke": 1.75, "john": 1.25},
         2: {"mateo": 3.00, "marcos": 1.50, "lukas": 1.25, "juan": 1.25}}


for batchnum in batch.keys():
    for name, grade in batch[batchnum].items():
        print("Batch Number:",batchnum, "Name: " + name + " Grade:", grade)
"""

#
# File Handling
#
"""
#create file
f = open("NewFile.txt", "x")

#write on file
f = open("NewFile.txt", "w")
f.write("hello world")

#append on file
f = open("NewFile.txt", "a")
f.write("\n This is additional line")
f.close()
"""
"""
q1 = "What I like about python is the learning curve, it's extremely easy to understand and " \
     "from what I've heard, python is so much faster than other programming languages."
q2 = "After learning python, I am planning to learn its frameworks like flask and django"
q3 = "I think I can apply what I've learned here on other programming languages I use, " \
     "the simplicity and organized approach of python"
q4 = "My goal is to master python programming and to use is to develop an application or" \
     " website that will empower all programmers"

f = open("questions.txt", "w")
f.write("What do I like about python? \n" + q1)
f = open("questions.txt", "a")
f.write("\n\nWhat do I plan to do after learning python? \n" + q2)
f.write("\n\nHow do I apply what I've learned?? \n" + q3)
f.write("\n\nWhat are my goals? \n" + q4)
f.close()
"""

#
# Reading from a file/deleting a file
#
"""
f = open("questions.txt", "r")

print(f.read())
print(f.readline())

for x in f:
     print(x)

f.close()
"""
"""
if os.path.exists("questions.txt"):
     os.remove("questions.txt")
     print("Successfully deleted!")
else:
     print("The file does not exist")
"""

#
# Exception
#
"""
x = 500
if x > 100:
     raise Exception("X should not be greater than 100!!!")
"""
"""
try:
     print(variable_1)
except NameError:
     print("The variable is not initialized or declared")
"""
"""
try:
     print(6*12)
except:
     print("The operation cannot be performed")
else:
     print("The operation can be performed!")
"""
"""
best_burger = "Burger King"
number_2_burger = "McDonald's"

assert best_burger == "Burger King"
assert best_burger == number_2_burger
"""

#
# Using Modules
#
"""
#f = open("functionfile.py", "x")
#imported from functionfile.py
convert = functionfile.convertUSDtoPHP(135)

print(convert)
"""

#
# built-in python modules
#
"""
#prints all the available built-in module
help("modules")

#prints a specific module
help("random")

#returns valid attributes of an object
print(dir(help("random")))
"""
"""
datenow = datetime.datetime.now()

print(datenow.year)
print(datenow.strftime("%B"))
print(datenow.day)

random = random.randint(1,100)

print(random)
"""