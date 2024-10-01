x=int(input("Enter a number: "))
z=" "
z1="#"
for i in range(x,0,-1):
  print(i*z1)
print()
print("--8<--"*10)

y=int(input())
y2=y/2
z*=y2
for i in range(y):
  print(f"{z} {z1} {z}")
  for i in range (2):
    z1+="#"
