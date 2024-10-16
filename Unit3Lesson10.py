import math#importing math library for calculations :]
x=(input("Enter an integer greater than 2: "))#taking input from the user
q=0#creating a variable q and setting it to 0 for the try and except statement
try:#declaring try function
  x=int(x)#trying to convert x to int to check if it is the correct data type
except:#declaring except function
  print("Bad input")#telling the user there input is incorrect
  q+=1#incrimenting q variable to stop further code
if(q==0):#checking if q is 0 to confirm int data type
  if(x-3<0):#using if statment to check that x-3 is less than 0 to check if its not meeting parameters
    q+=1#incrimenting q variable to stop further code
    print("Bad input")#telling the user there input dose not meet parameters
if(q==0):#checking that q is 0 to confirm the input is correct
  for i in range (3,x+1):#using a for loop starting at 3 up to the users input to print each triple
    if(i%2==1):#checking if i is odd in this occurance to use the correct formula
      z=i**2+((i//2*(i+1))**2)#doing calculations to find the 2nd number in the triple squared + the 1st number in the triple squared
      y=(i//2*(i+1)+1)**2#doing calculations to find the 3rd number in the triple squared
      if(z==y):#checking that a^2+b^2=c^2
        v=int(math.sqrt(z-(i**2)))#converting z into only the second number of the triple
        w=int(math.sqrt(y))#converting y into the 3rd number in the triple
        print("%d, %d, %d" %(i,v,w))#printing the triple formated
        print("_______________________")#printing a divider for easier readability
    elif(i%2==0):#checking if i is even in this occurance to use the correct formula
      m=int(i**2/4)#calculating a number in between the 2nd and 3rd triples
      b=m-1#finding the 2nd number through m
      c=m+1#finding the 3rd number through m
      print("%d, %d, %d" %(i,b,c))#printing the triple formated
      print("_______________________")#printing a divider for easier readability
