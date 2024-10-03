progname = "Duis sodales, arcu eu faucibus varius, nibh justo placerat nibh."#Text from lipsum
y=0#variable to store spaces
for x in progname:#for loop to run through each character in the text
  if(x==" "):#if statment to check for spaces
    y+=1#adding to y variable if it identifies a space
print("The text is",progname)#giving the user the text
print("There are",y,"spaces in the text.")#displaying the number of spaces for the user
