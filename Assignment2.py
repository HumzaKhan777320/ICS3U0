#not done yet
import math
print("Hello, welcome to the school yearbook program here you will be asked to enter a number of photos and it will return you the most efficient dimensions of how to organize your number of photos photos.\n")
y=True
while y:
    n=0
    x=(input("Enter the number of photos you would like organized: "))
    if(x=="Done"or x=="done"):
        print("Thank you for using the school yearbook program by Humza Khan we hope you found it helpful and please feel free to contact us at (###)###-#### for any questions or concerns")
        break
    try:
        if(n==0):
            x=int(x)
            if(x>0):
                v=[]
                z=math.sqrt(x)
                z=math.floor(z)
                for i in range(z):
                    if(x%(i+1)==0):
                        v.append(i+1)
                v1=v[-1]
                q=int(x/v1)
                p=(v1*2)+(q*2)
                print("It would look like this:")
                for i in range(q):
                    for i in range(v1):
                        print("#",end = "")
                    print()
                print("%d x %d with perimeter %d" %(q,v1,p))
            else:
                n+=1
                print(f"Sorry {x} is invalid input try a positive integer")
    except:
        print("Sorry your input is invalid")
        n+=1
