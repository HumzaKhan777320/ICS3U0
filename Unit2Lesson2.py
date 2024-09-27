import math # importing math library

x = input("Please input a whole number between 1 and 20: ") #Taking input from user
x = int(x) # Turning input into int
if(x>=1 and x<=20): #using if statment to check input is in parameters
  y = input("Please input another nonzero whole number between 1 and 20: ") #Taking second input
  y = int(y) # Turning input into int
  if(y>=1 and y<=20): #using if statment to check input is in parameters 
    print("Now deciding if", y, "is a factor of", x, "...")
    if(y!=0): #using if statement to check for error output
      rem = x % y
    else:
      print("You cannot enter 0 as a divider") #givig user output
    if (rem == 0): # checking for calculatipon using if statement
      print("Yes!", y, "is a factor of", x) #givig user output
    else:
      print("Nope", y,"is not a factor of",x) #givig user error output
  else:
    print("Not in range") #givig user error output
else:
  print("Not in range") #givig user error output
