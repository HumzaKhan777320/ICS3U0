import math 
def add(a, b):
  try:
    a=float(a)
  except:
    print("Bad data")
  try:
    b=float(b)
  except:
    print("Bad data")
  return a + b
a=input("Enter a number: ")
b=input("Enter a number: ")
print(add(a,b))

def mypow(m,n):
  try:
    m=float(m)
  except:
    print("Bad data")
  try:
    n=float(n)
  except:
    print("Bad data")
  return math.pow(m,n)
m=input("Input a number: ")
n=input("Input a number: ")
print(mypow(m,n))
