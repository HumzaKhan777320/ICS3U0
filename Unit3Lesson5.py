import math #importing the math library for calculations later
def add(a, b):#creating an add function with 2 parameters
  try:#creting a try function
    a=float(a)#trying to convert a variable to float to check if its correct input
  except ValueError:#creating an except function
    return "Bad data"#returning bad data if the data type is infavorable
  try:#creting a try function
    b=float(b)#trying to convert b variable to float to check if its correct input
  except ValueError:#creating an except function
    return "Bad data"#returning bad data if the data type is infavorable
  return a + b#returning the 2 variables added together 
  
a=input("Enter a number: ")#taking an input from the user and storing it inside a variable
b=input("Enter a number: ")#taking an input from the user and storing it inside b variable
print(add(a,b))#printing the return from the add function with the given inputs as parameters

def mypow(m,n):#creating a mypow function with 2 parameters
  try:#creting a try function
    m=float(m)#trying to convert m variable to float to check if its correct input
  except:#creating an except function
    return "Bad data"#returning bad data if the data type is infavorable
  try:#creting a try function
    n=float(n)#trying to convert n variable to float to check if its correct input
  except:#creating an except function
    return "Bad data"#returning bad data if the data type is infavorable
  return math.pow(m,n)#returning m to the power of n
  
m=input("Input a number: ")#taking an input from the user and storing it inside m variable
n=input("Input a number: ")#taking an input from the user and storing it inside n variable
print(mypow(m,n))#printing the return from the mypow function with the given inputs as parameters
