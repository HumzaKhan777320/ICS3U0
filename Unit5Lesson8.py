def validate(N):
  total=0
  a=len(N)
  N=str(N)
  for i in range(0,a,2):
    add=int(N[a-i-2])*2
    if(i+2)<a:
      if(add<10):
        total+=add
      else:
        total+=add-9
  for i in range(0,a,2):
    total+=int(N[i])
  if(total%10==0):
    return True
  else:
    return False

print("Validate a number with the Luhn Algorithm!")
num = input("Input a number to validate: ")
isValid = validate(num)
if isValid:
    print(num, "is valid!")
else:
    print(num, "is not valid!")
