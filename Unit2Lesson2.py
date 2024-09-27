import math

x = input("Please input a whole number between 1 and 20: ")
x = int(x)
if(x>=1 and x<=20):
  y = input("Please input another nonzero whole number between 1 and 20: ")
  y = int(y)
  if(y>=1 and y<=20):
    print("Now deciding if", y, "is a factor of", x, "...")
    if(y!=0):
      rem = x % y
    else:
      print("You cannot enter 0 as a divider")
    if (rem == 0):
      print("Yes!", y, "is a factor of", x)
    else:
      print("Nope", y,"is not a factor of",x)
  else:
    print("Not in range")
else:
  print("Not in range")
