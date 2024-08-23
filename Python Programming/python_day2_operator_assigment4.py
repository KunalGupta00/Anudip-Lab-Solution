#Q.4. Python program to find the area of a triangle whose sides are given.

import math

a = int(input("Enter length of side a :"))
b = int(input("Enter length of side b :"))
c = int(input("Enter length of side c :"))

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * ( s - c))

print("The Area of a triangle is : ",area)

"""
Ans : Enter length of side a :10
         Enter length of side b :2
         Enter length of side c :11
         The Area of a triangle is :  9.051933495115836
"""
