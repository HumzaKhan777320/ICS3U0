import math # Importing math library
radius = int(input("Please input radius: ")) # Getting radius from user
radius_squared=math.pow(radius,2) # Squaring radius for area of semi-circle
square_length=(2*radius) # Setting square length with radius since the diameter of the semi-circle = the square length
square_area=math.pow(square_length,2) # Finding the area of the squaqre from square_length
half_circle_area=0.5*radius_squared*math.pi # Finding area of semi-circle with inputed radius
total_area=square_area+half_circle_area # Calculating total area by adding the two shpaes areas
print("Area is:", total_area) # Printing total area
