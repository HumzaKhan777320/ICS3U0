#not done yet
import turtle

def plot(x,y,z,color):
    x+y+z+color

filename = "test1.xpm"
fh = open(filename, "r")
colorLine = fh.readline() 
colorLine.strip()
row, col, num = colorLine.split()
row=int(row)
col=int(col)
numColors=int(num)
colorDefs = [[0]*2]*numColors
print("There are",row,"rows")
print("There are",col,"columns")
print("There are",numColors,"colors")
c1=[[0]]*numColors
for i in range(numColors):
    colorLine = fh.readline() 
    colorLine.strip()
    sym, c, color = colorLine.split()
    if(sym=="~"):
        sym=" "
    colorDefs[i][0] = sym
    colorDefs[i][1] = color
    print(colorDefs[i][0],":",colorDefs[i][1])
    c1[i]=[colorDefs[i][0],colorDefs[i][1]]
x=0
if(row<=col):
    x=col
else:
    x=row
a=[0]*x
print(c1)
for j in range(x):
    for i in range(x):
        if(j==0):
            a[i]=fh.readline()
            print(a[i],end="")
        turtle.penup()
        turtle.goto(x/2+(i*10), x/2-(j*10))
        turtle.pendown()
        for l in c1:
            if l[0]==a[j][i]:
                k=l[1]
        turtle.dot(10,k)
fh.close()
