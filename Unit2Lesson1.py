print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
elif(ch=="C"):
    print("I prefer cherries")
else: 
  print("Error input")

x=int(input("Enter a number between 1 and 100: "))
if(x>=80 and x<=100):
  print("A")
if(x>=70 and x<=79):
  print("B")
if(x>=60 and x<=69):
  print("C")
if(x>=50 and x<=59):
  print("D")
if(x<50):
  print("F")
else:
  print("Error input")
