# Basic learnings about the python  syntax

# food=input("what is your favorite food ?\n")
# print("oh! so your fav food is "+food+" that's cool")
# #this is to sum two numbers
# no1=int(input("enter first number = \n"))
# no2=int(input("enter second number = \n"))
# sum_2=no1+no2
# print(f"your total is {sum_2}")
# if sum_2 >= 50:
#     print("number is greater than 50 ")
# else:
#     print("number is smaller than 50 ")
# name=input("what is your name?\n ")
# print(f"hello {name}")

#Calculate the area of the shapes
# import math
# print("enter r for rectangle, c for circle, s for square, t for triangle\n")
# shape=input("enter shape you want to calculate area for")
# if shape == "r":
#     l=float(input("enter the length in cm: "))
#     w=float(input("enter the width in cm: "))
#     print(f"area = {l*w}cm²")
# elif shape == "c":
#     r=float(input("enter the radius in cm: "))
#     print(f"area = {math.pi*r*r}cm²")
# elif shape == "s":
#     s=float(input("enter the side length in cm: "))
#     print(f"area = {s*s}cm²")
# elif shape == "t":
#     b=float(input("enter the base in cm: "))
#     h=float(input("enter the height in cm: "))
#     print(f"area = {0.5*b*h}cm²")
# else:
#     print("enter the right initials you dummy")


# Arithmatic operators
# - = subtracting
# * = multiply
# / = divide
# ** = power of the variable
# % = module to get the reminder

# inbuilt math functions
# round(x) round of the number
# abs(x) absolute value the number
# pow(base,power) to get the power of the base
# max(x,y,a,z) to get the maximum no. b/w variables
# min(x,y,z,a) to get the minimum no. b/w variables
# import math
# math.pi for value of pi
# math.sqrt(x) to get the square root of the variable
# math.ceil(x) round up the float no.
# math.floor(x) round down the float no.

#area of the circle
# import math
# r=float(input("enter the radius in cm: "))
# print(f"area = {math.pi * pow(r,2)}cm²")

# Hypotenuse of right triangle
# hypotenuse=square root of height²+base²
# import math
# height=float(input("enter the height: "))
# base=float(input("enter the base: "))
# hypotenuse=math.sqrt(pow(height,2)+pow(base,2))
# print(hypotenuse)

#if statement, else-if statement, else statement

# name=input("enter your name = ")
# if name == "":
#     print("enter the fucking name!!!!")
# else:
#     print(f"hello {name}")