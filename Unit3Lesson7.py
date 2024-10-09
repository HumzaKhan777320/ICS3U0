def comp(S):#defining a function that takes parameter S
  z=""#creating an empty string to store the output
  for i in range(len(S)):#creating a for loop that runs through each letter in string S
    if(S[i]=="A"):#checking if a letter is A
      x.append("T")#Replacing A with T and adding it to x array
    if(S[i]=="T"):#checking if a letter is T
      x.append("A")#Replacing T with A and adding it to x array
    if(S[i]=="C"):#checking if a letter is C
      x.append("G")#Replacing C with G and adding it to x array
    if(S[i]=="G"):#checking if a letter is G
      x.append("C")#Replacing G with C and adding it to x array
    z=z+x[i]#adding the new letter from array x to string z
  return(z)#returning the new string z
  

x=[] #empty array to store the new letters of the string given
y=input("Enter DNA strand")#taking input of the DNA strand from the user
print(comp(y))#printing the comp function with parameter y
