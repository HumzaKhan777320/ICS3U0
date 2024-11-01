import random as r
def shuffle(A):
    for i in range(len(A)):
      temp=A[i]
      j=r.randint(0,len(A)-1)
      A[i]=A[j]
      A[j]=temp
    return A
    

size = int(input("Enter the size of the array"))
B = []
for i in range(1,size+1):
  B.append(i)

print(B) 
B = shuffle(B)
print(B) 
