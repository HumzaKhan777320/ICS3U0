items = []#empty array to store the strings the user enters later on
x=int(input("How many items are you entering? "))#asking the user the number of items their entering to implement in a loop later on 
print(("Enter your items now:"))#printing a statment to tell the user to print the items after per the example
for i in range(x):#creating a for loop to allow the user to enter the number of items they want
  y=input("Next item: ")#taking input from the user and providing instructions
  items.append(y)#taking the users inputed item and storing it in the above empty array
print("You have entered",len(items),"items.")#printing the numbers of items in the list for the user 
for i in range(len(items)):#creating a for loop to print each item in the list
    print(items[i])#printing each item in the list for the user
