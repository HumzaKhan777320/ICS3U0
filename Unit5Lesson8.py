#not done
def validate(N):
  total=0
  a=len(N)
  N=str(N)
  for i in range(0,a+1,2):
    print(i)
    total+=int(N[a-i])*2
  for i in range(0,a,2):
    total+=int(N[i])
  if(total%10==0):
    isValid=True
  else:
    isValid=False

print("Validate a number with the Luhn Algorithm!")
num = input("Input a number to validate: ")
isValid = validate(num)
if isValid:
    print(num, "is valid!")
else:
    print(num, "is not valid!")
