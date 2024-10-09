def factorize(N):#creating a factorize function that takes 1 parameter
  v=[]#emptying the v array for next calculation
  if(N==0):#checking if N is 0 because it needs a specific output
    v.append(0)#appending 0 as the factors of 0
  elif(N==1):#checking if N is 1 because it needs a specific output
    v.append(0)#appending 0 as the factors of 1
  for i in range(1,N):#creating a for loop to check for factors of N appart from N itself
    if N%i==0:#checking for a remainder using % to see if the current value of i is a factor of N
      v.append(i)#appending i to v if its a factor
  return(sum(v))#returning the array v after runned with the sum function
  
v=[]#declaring an empty array for storing factors
z=0#creating a variable to store the factor sum
def sum(x):#defining the sum function that takes 1 parameter
  z=0#emptying the z value for the calculation
  for i in range(0,len(x)):#creating a for loop to go through each element in the given array
    z+=x[i]#adding the ith index of the given array to z without adding 1 to i because bot indexes and for loops start with 0
  return(z)#returning z which holds the factor sum

d=0# creating a variable and setting it to 0 for the try function to come
  
x1=input("Enter a number: ")#taking input from the user
try:#declaring a try function
  x1=int(x1)#converting x1 to int to check if its actually an int
except:#declaring except function
  print("This is not an integer")#telling the user they gave wrong input
  d+=1#adding 1 to d variable so further calculations dont happen with bad data types
if(d==0):#creating if statement so calculations only happen with the correct data type
  if x1>=0:#checking that x1 is greater than 0
    print("Factor sum: %d" % factorize(x1))#printing the factor sum for the user 
    if(x1==factorize(x1)):#checking if the inputed number is perfect
      print("%d is perfect" %x1)#outputing that the number is perfect if it is
    if(x1>factorize(x1))::#checking if the inputed number is deficient
      print("%d is deficient" %x1)#outputing that the number is deficient if it is
    if(x1<factorize(x1))::#checking if the inputed number is abundant
      print("%d is abundant" %x1)#outputing that the number is abundant if it is
  else:#else statement
    print("Goodbye:(")#printing goodbye if the inputed number is < 0 

