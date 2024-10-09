io = int(input("Enter a number to get factorials up to it: ")) #Variable for storing the value of a number asked from the user to print the certain ammount factorials
x=1 #creating variable to store factorials
y=2 #creating variable to incriment to find factorials
z=0 #setting variable for while loop
while(z<=io): #creating while loop to print factorials
  print(z,"!=", x, sep = "") #outputing factorials for user
  x=x*y #calculating factorials and storing in x
  y+=1#incrementing y for next calculation
  z+=1#incrementing z to at some point end while loop
