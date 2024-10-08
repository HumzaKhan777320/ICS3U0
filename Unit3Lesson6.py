def factorize(N):
  v=[]
  if(N==0):
    v.append(0)
  elif(N==1):
    v.append(0)
  for i in range(1,N):
    if N%i==0:
      v.append(i)
  
v=[]

def sum(x):
  z=0
  for i in range(0,len(x)):
    z+=x[i]
  return(z)
  
print(factorize(6))
print(factorize(24))
print(factorize(0))
print(factorize(1))
print(factorize(7))
