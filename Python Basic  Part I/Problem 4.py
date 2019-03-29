# Write a Python program which accepts the radius of a circle from the user and compute the area.

"""
Formula: area = pi * r * r
"""
from math import pi

r = float(input("Enter the radius of circle: "))
area = pi * r ** 2
print(f"Area = {area}")
