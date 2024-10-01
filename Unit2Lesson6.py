x=int(input("Enter a number: ")) # taking an input from the user to make the wanted size upside down half triangle 
z=" " #variable to store empty space for loops later on
z1="#" #variable to store a hashtag for loops later on
for i in range(x,0,-1): #for loop for printing out the upside down half triangle and starting at given variable and going down to 1
  print(i*z1) #printing the hashtags based on the calculation done with the for loop
print("--8<--"*10) #printing a dividor for the next lines of code

#****************************************(Divider for code for easy readability)

y=int(input("Enter a number: ")) # taking an input from the user to make the wanted size triangle/pyramid
for i in range(y): # making a for loop to print the wanted number of levels of the pyramid
    print(z*(y-i-1), end="") #doing calculations based on the current number of the loop and the given input also making sure the print line dosnt end to print the next line in the same space
    print(z1*(i*2+1)) #doing calculations based on the current value of the for loop and printing it after the spacing in the previous line for formatting
print("--8<--"*10)  #printing a dividor for the next line of code

#****************************************(Divider for code for easy readability)

z2=int(input("Enter a number: ")) # taking an input from the user to make the wanted size diamond/rombus
for i in range(z2): #making a for loop to create a triangle similar to the last code 
    print(z*(z2-i-1), end="") #doing calculations based on the current number of the loop and the given input also making sure the print line dosnt end to print the next line in the same space
    print(z1*(i*2+1))#doing calculations based on the current value of the for loop and printing it after the spacing in the previous line for formatting
for i in range(z2-2,-1,-1): #making a for loop to create the bottom half of the rombus similar to the first code with a dash of the second :) 
    print(z*(z2-i-1), end="") # doing calculations based on the input and the curent value of the for loop(i) for spacing to format the bottom part of the rombus
    print(z1*(i*2+1))# doing calculations to print the hashtags based on the current value of the for loop
        
