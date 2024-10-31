# Name: Humza Khan
#Student Number: 777320 
#Course Code: ICS3U0 
#Assignment: Programming Assignment 2: School Yearbook
#10/29/2024

#8<-----8<-----8<-----8<-----8<-----8<-----8<-----8<-----8<-----8<-----8<-----

#Variable library:

#myfunc - name of the function that returns an array of the the first
    #half factors of its 1 parameter user_inpt

#user_inpt - is used as a parameter in the function myfunc
    #and a variable to store the users input in the main code

#arr - variable to store an array with the first half factors of the users input
    #in order of least to greatest in the myfunc function

#z - variable used for storing a number up to which factors of user_inpt will be stored in arr

#i - variable to increment i times from 0 for a for-loop and to use to find factors

#tf - boolean variable used for the main while loop (acts as an on and off switch)

#n - variable set to 0 to add to in case of error input
    #but not ending the loop to prevent errors

#v1 - variable used to store the last factor of the array arr
    #from function myfunc with parameter user_inpt

#q - variable to store the other dimension of the most perimeter efficient
    #rectange of the photos calculated with user_inpt and v1

#p - variable to store the perimeter of the rectangle of photos
    #with the dimensions found and stored in v1 and q

#j - variable that increments q times to print each row in the example image

#k - variable that increments v1 times to print the correct number of #s in each row

#8<-----8<-----8<-----8<-----8<-----8<-----8<-----8<-----8<-----8<-----8<-----

#imports
import math#importing math library for calculations of perimeter

#function
def myfunc(user_inpt):#defining a function with 1 parameter user_inpt
  arr=[]#creating an array to store the first half factors of user_inpt 
  z=math.sqrt(user_inpt)#storing the sqrt of user_inpt in z
  z=math.floor(z)#flooring the sqrt of user_inpt into an int
  for i in range(z):#going through each int from 0 to z
    if(user_inpt%(i+1)==0):#checking if the current value of i+1 is a factor of user_inpt
        arr.append(i+1)#appending i+1 to arr
  return(arr)#returning arr array

#welcome statement and details
print("Hello, welcome to the school yearbook program", end="")
print(" here you will be asked to enter a number of photos",end="")
print(" and it will return the most efficient dimensions",end="")
print(" on how to organize them.\n")
#printing a message for the user to give details of the program
print("If you ever wish to exit the program please enter done or Done instead of a number\n")
#Giving the user instructions on how to exit the program

tf=True#setting tf to true for while loop

#main loop
while tf:#creating while loop to run until the user enters done
    
    n=0#setting n to 0 to run the code later on
    #and to stop the code from running by changing the variable
    
    user_inpt=(input("Enter the number of photos you would like organized: "))
    #taking input from the user and storing it in user_inpt
    
    if(user_inpt=="Done"or user_inpt=="done"):#checking if the user enters done or Done
        print("Thank you for using the school yearbook program by Humza Khan",end="")
        print(" we hope you found it helpful and please feel free to contact us",end="")
        print(" at (###)###-#### for any questions or concerns.")
        #printing a message for the user as they leave the program
        break#ending the loop
    
    try:#declaring try function
        if(n==0):#checking that n = 0 to make sure the input is valid(positive int)
            user_inpt=int(user_inpt)#turning user_inpt into an integer
            if(user_inpt>0):#checking that user_inpt is greater than 0(extra precaution)
                v1=myfunc(user_inpt)[-1]
                #storing the last factor of user_inpt listed in arr from myfunc into v1 
                q=int(user_inpt/v1)#using user_inpt and v1 to find the other dimension
                #and storing in q
                p=(v1*2)+(q*2)#using v1 and q to find the perimeter and store it in p
                
                print("It would look like this:")
                #printing a message to the user to title the following image
                for j in range(q):#going through each line of printing
                    for k in range(v1):#going through each element of printing
                        print("#",end = "")#printing a hashtag for each photo
                    print()#ending the line for the next row
                    
                print("The most perimeter efficient dimensions of %d photos" %(user_inpt),end="")
                print(" is %d x %d with a perimeter of %d." %(q,v1,p))
                #printing the dimensions of the rectangle of photos and the perimeter of it
                
            else:#else statment to activate if user_inpt is <=0
                n+=1#incrimenting n to stop the code
                print(f"Sorry {user_inpt} is invalid input try a positive integer")
                #telling the user that there input is invalid and a suggestion for later
    except:#expect function
        print("Sorry your input is invalid")#telling the user there input is invalid
        n+=1#incrimenting n to stop the code
