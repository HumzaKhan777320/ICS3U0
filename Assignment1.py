# Name: Humza Khan Student Number: 777320 Course Code: ICS3U0 Assignment: Programming Assignment 1 Three-Part Python Output with Math
import math as m # importing math library for calculations and using it as m for simplicity

print("1:") # Indicator that its the first part of the assignment
length_rectangle = float(input("Enter the length of a rectangle to find its area. Do not enter any units just the number: ")) # Taking the length of the rectangle from the user giving instructions
width_rectangle = float(input("Enter the width of a rectangle to find its area. Do not enter any units just the number: ")) # Taking the width of the rectangle from the user giving instructions
area_rectangle = length_rectangle*width_rectangle # calculating the area of the rectangle
print("The area of the rectangle with length %.2f and width %.2f is %.2f units squared"%(length_rectangle, width_rectangle,area_rectangle)) # displaying the area of the rectangle to the user and explaining to them what it is
print("\n*********************************************************************************") # divider for simplicity when reading also indicating new calculation

print("2:")# Indicator that its the second part of the assignment
radius_circle = float(input("Enter the radius of a circle that you want the area of: "))# Talking the radius of the circle from the user and giving instructions
area_circle = m.pow(radius_circle,2)*m.pi # calculating the area of the circle
print("The area of the circle with radius %.2f is %.2f units squared"%(radius_circle, area_circle)) # displaying the area of the circle for the user and interprits it for the user 
print("\n*********************************************************************************")# divider for simplicity when reading also indicating new calculation

print("3:")# Indicator that its the third part of the assignment
radius_cylinder = float(input("Enter the radius of a cylinder to find its surface area and volume. Do not enter any units just the number: "))#Talking the radius of the cylinder from the user and giving instructions
height_cylinder = float(input("Enter the height of a cylinder to find its surface area and volume. Do not enter any units just the number: "))#Talking the height of the cylinder from the user and giving instructions
surface_area=2*m.pi*radius_cylinder*height_cylinder+2*m.pi*m.pow(radius_cylinder,2) # calculating the surface area of the cylinder
volume=m.pi*m.pow(radius_cylinder,2)*height_cylinder# calculating the volume of the cylinder
print("The surface area of the cylinder with radius %.2f and height %.2f is %.2f units squared"%(radius_cylinder, height_cylinder, surface_area))# printing the surface area of the cylinder and interpreting it for the user
print("The volume of the cylinder with radius %.2f and height %.2f is %.2f units cubed"%(radius_cylinder, height_cylinder, volume))# printing the volume of the cylinder and interpreting it for the user
print("\n*********************************************************************************") # divider for simplicity when reading also indicating new calculation

print("4:")# Indicator that its the fourth part of the assignment
length_pendulum = float(input("Enter the length of the pendulum to find the time it takes for 1 swing. Do not enter any units just the number: "))#Talking the length of the pendulum from the user and giving instructions
time_for_swing = 2*m.pi*m.sqrt(length_pendulum/9.8) # calculating the time it takes for the swing
print("The time it takes for 1 swing of the pendulum with length %.2f is %.2f seconds" %(length_pendulum, time_for_swing))# presenting the time to the user and explaining it
print("\n*********************************************************************************")# indicating the end of the code
