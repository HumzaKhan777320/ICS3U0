items = ["Apples", "Bananas", "Cherries", "Dosa"]#array/list full of different fruits
sizes = []#empty narray to store the correct sizes of the strings
y=[]#empty array to store what the user thinks the size is
for i in range(len(items)): #using a for loop to run through each element in items
    sizeI = len(items[i])#storing the size of an element to a variable
    sizes.append(sizeI)#putting the correct size into the sizes array

for i in range(len(items)):#for loop to run through each element in items
  print("Enter the size of",items[i],": ",end="")#giving the user instructions to enter the size of a string
  z=int(input())#taking input from the user(what they think the size is)
  y.append(z)#storing the users input inb an empty array
  if(y[i]==sizes[i]):#using an if statment to check if the user's guess is correct
    print("Since %s has a size of %d this is True" % (items[i], y[i]))#telling the user they are correct iof the if statment is true
  else:#declaring an else statment to print something if the user's guess was wrong
    print("Since %s does not have a size of %d this is False" % (items[i], y[i]))#error output for the user telling them their guess was incorrect
