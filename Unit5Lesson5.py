def fib(n):
    if(n==0):
        return(0)
    if(n==1):
        return(1)
    else:
        a=fib(n-1)+fib(n-2)
        return a
    
def whole(n):
    try:
        n=int(n)
        if(n==0):
            print(fib(0))
        else:
            for i in range(1,n+1):
                print(fib(i),end=" ")
    except:
        print("Soory you did not input a whole nuber plese try again")

print("Program for printing the Fibonacci sequence!")
x=input("Please input a whole number: ")
if int(x)<0:
    print("Sorry no negative numbers try again")
else:
    whole(x)
