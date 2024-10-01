x=int(input("Enter a whole number >0")) #Taking input from user
z=1 #creating variable to store triangular numbers
z1=1 #creating variable to store factorials
y=2 #creating variable to create new triangular numbers
y1=2 #creating variable to create new factorials 
print("Counting from 1 to",x)#Printing explanation of further output
print("#  tri   factorial") #printing titles of columns for user
for i in range(x): #creating for loop for calculations and printing
  z+=y # calculating triangular numbers
  y+=1 # incrementing y variable for next calculation
  z1*=y1 # calculating factorials
  y1+=1 # incrementing y1 variable for next calculation
  print("%2d %5d %10d"%((i+1),z,z1)) #printing out the number of calculation, the triangular number, and factorial, and formating
