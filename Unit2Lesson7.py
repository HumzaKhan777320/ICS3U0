import math as m #importing math library for calculations and using it as m for simplicity
b=10 #setting a variable with 10 to increment by 15 later on to print values of n from 10 - 200 in steps of 15
y=0# setting a variable to store the number when squared
z=0# setting a variable to store the number when cubed
a=0# setting a variable to store the number when squae rooted
print("  N|  SQR|  Cubes|Roots")#printing labels for columns per the example
print("---+-----+-------+-----")#printing dividers for columns and titles per the example
while(b<200):# creating a while loop to keep printing values starting from 10 and stopping at 200 
  y=m.pow(b,2)# setting y to the value of N/b squared via math library
  z=m.pow(b,3)# setting z to the value of N/b cubed via math library
  a=m.sqrt(b)# setting a to the value of N/b square rooted via math library
  print("%3d| %4d| %6d| %4.2f"%(b,y,z,a))# printing for the user each row with formating
  b+=15#incrimenting variable b or N by 15 to count by steps of 15
