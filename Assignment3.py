#not done yet
import turtle
turtle.tracer(0,0)   
def plot(x,y,z,color):
    x+y+z+color

filename = "rocky_bullwinkle_mod.xpm"
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
x=col
y=row
a=[0]*x
for j in range(x):
    for i in range(y):
        if(j==0):
            a[i]=fh.readline()
        turtle.tracer(0,0)
        turtle.penup()
        turtle.goto(y*-3/2+(i*3), x*3/2-(j*3))
        turtle.pendown()
        for l in c1:
            if l[0]==a[j][i]:
                print(a)
                k=l[1]
        turtle.dot(3,k)
        turtle.hideturtle()
turtle.update()
fh.close()
