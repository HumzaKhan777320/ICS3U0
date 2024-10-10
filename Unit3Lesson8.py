#This time I kept the function at the top of the code
def validate(S):#defining a function that takes 1 parameter S
  x=[]#creating an empty array to hold the position of incorrect elements in S
  y=[]#creating an empty array to hold incorrect elements in S
  z="Not valid: "#String to hold error statements
  for i in range(len(S)):#creating a for loop that goes through each letter in S
    if(S[i]!="A" and S[i]!="T" and S[i]!="C" and S[i]!="G"):#checking for incorrect letters in S
      x.append(i+1)#appending the position of an error to the array x based on the current value of i
      y.append(S[i])#appending an errored element to the array y based on the current value of i
  if(len(y)==0):#checking is there are no error elements identified
    return "Valid"#returning valid if no error elements identified
  else:#declaring else statment
    for i in range (len(y)):#runing a for loop to run through each incorrect element if there is atleast 1 element
      z=z+"\n%s found in position %d. " %(y[i], x[i])#adding the wrong element and opsitio the the error string
    return z#returning the error string if there is atleast 1 element in the error string

w=int(input("How many DNA strands do you want to enter: "))#taking input from the user to see how many DNA strands they want to enter
for i in range(w):#using a for loop to take the desired number of DNA strands from the user(not actual DNA strands just ones incoded with letters)
  v=input("Enter a DNA strand: ")#taking the DNA strands from the user
  print(validate(v))#printing the return of the valadate function when run with v
