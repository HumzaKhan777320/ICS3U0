def f(n):
    if(n==0):
        return(0)
    if(n==1):
        return(1)
    else:
        a=f(n-1)+f(n-2)
        return a
def whole(n):
    for i in range(n+1):
        print(f(i),end=" ")
    return ""
x=int(input("Enter an integer to get the numbers in the Fibonacci up to your input: "))
print(whole(x))
