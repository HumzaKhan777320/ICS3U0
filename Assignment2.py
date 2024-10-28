#not done yet
# Name: Humza Khan
#Student Number: 777320 
#Course Code: ICS3U0 
#Assignment: Programming Assignment 2: School Yearbook
#10/23/2024
import math#importing math library for calculations of perimeter
def myfunc(x):#defining a function with 1 parameter x
  v=[]#creating an array to store the factors of x 
  z=math.sqrt(x)#storing the sqrt of x in z
  z=math.floor(z)#flooring the sqrt of x into an int
  for i in range(z):#going through each int from 0 to z
    if(x%(i+1)==0):#checking if the current value of i+1 in a factor
        v.append(i+1)#appending i+1 to v
  return(v)#returning v array
print("Hello, welcome to the school yearbook program here you will be asked to enter a number of photos and it will return you the most efficient dimensions of how to organize your number of photos.\n")#printing a message for the user to give details of the program
print("If you ever wish to exit the program please enter done or Done instead of a number\n")#Giving the user instructions on how to exit the program
y=True#setting y to true for while loop
while y:#creating while loop to run until the user enters done
    n=0#setting n to 0 to run the code later on and to stop the code from running by changing the variable
    x=(input("Enter the number of photos you would like organized: "))#takiong input from the user and storing it in x
    if(x=="Done"or x=="done"):#checking if the user enters done and wants to leave the program
        print("Thank you for using the school yearbook program by Humza Khan we hope you found it helpful and please feel free to contact us at (###)###-#### for any questions or concerns")#printing a message for the user as they leave the program
        break#ending the loop
    try:#declaring try function
        if(n==0):#checking that n = 0 to make sure the input is valid(positive int)
            x=int(x)#turning x into an integer
            if(x>0):#checking that x is greater than 0(extra precaution)
                v1=myfunc(x)[-1]#storing the last factor of x listed in v from myfunc into v1 
                q=int(x/v1)#using x and v1 to find the other dimension and storing in q
                p=(v1*2)+(q*2)#using v1 and q to find the perimeter and store it in p 
                print("It would look like this:")#printing a message to the user to tell them when x photos are organized perimeter efficient what it would look like
                for j in range(q):#going through each line of printing
                    for k in range(v1):#going through each element of printing
                        print("#",end = "")#printing a hashtag for each photo and not endingt the line so they are in a row
                    print()#ending the line for the next row
                print("%d x %d with perimeter %d" %(q,v1,p))#printing the dimensions of the rectangle of photos and the perimeter of it
            else:#else statment to activate if x is <=0
                n+=1#incrimenting n to stop the code
                print(f"Sorry {x} is invalid input try a positive integer")#telling the user that there input is invalid and a suggestion for the new input
    except:#expect function
        print("Sorry your input is invalid")#telling the user there input is invalid
        n+=1#incrimenting n to stop the code
