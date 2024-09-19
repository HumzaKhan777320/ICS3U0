import math
radius = int(input("Please input radius: "))
radius_squared=math.pow(radius,2)
square_length=(2*radius)
square_area=math.pow(square_length,2)
half_circle_area=0.5*radius_squared*math.pi
total_area=square_area+half_circle_area
print("Area is:", total_area)
