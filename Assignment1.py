import math as m

print("1:")
length_rectangle = float(input("Enter the length of a rectangle to find its area. Do not enter any units just the number: "))
width_rectangle = float(input("Enter the width of a rectangle to find its area. Do not enter any units just the number: "))
area_rectangle = length_rectangle*width_rectangle
print("The area of the rectangle with length %.2f and width %.2f is %.2f"%(length_rectangle, width_rectangle,area_rectangle))
print("\n*********************************************************************************")

print("2:")
radius_circle = float(input("Enter the radius of a circle that you want the area of: "))
area_circle = m.pow(radius_circle,2)*m.pi
print("The area of the circle with radius %.2f is %.2f"%(radius_circle, area_circle))
print("\n*********************************************************************************")

print("3:")
radius_cylinder = float(input("Enter the radius of a cylinder to find its surface area and volume. Do not enter any units just the number: "))
height_cylinder = float(input("Enter the height of a cylinder to find its surface area and volume. Do not enter any units just the number: "))
surface_area=2*m.pi*radius_cylinder*height_cylinder+2*m.pi*m.pow(radius_cylinder,2)
volume=2*m.pi*m.pow(radius_cylinder,2)
print("The surface area of the cylinder with radius %.2f and height %.2f is %.2f"%(radius_cylinder, height_cylinder, surface_area))
print("The volume of the cylinder with radius %.2f and height %.2f is %.2f"%(radius_cylinder, height_cylinder, volume))
print("\n*********************************************************************************")

print("4:")
length_pendulum = float(input("Enter the length of the pendulum to find the time it takes for 1 swing. Do not enter any units just the number: "))
time_for_swing = 2*m.pi*m.sqrt(length_pendulum/9.8)
print("The time it takes for 1 swing of the pendulum with length %.2f is %.2f seconds" %(length_pendulum, time_for_swing))
print("\n*********************************************************************************")
