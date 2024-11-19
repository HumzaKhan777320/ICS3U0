import turtle

t = turtle.Turtle()
def plot(x,y,z,color):
    x+y+z+color

filename = "cool_smiley_mod.xpm"
fh = open(filename, "r")
colorLine = fh.readline() 
colorLine.strip()
row, col, num = colorLine.split()
row=int(row)
col=int(col)
numColors=int(num)
colorDefs = [[0] * 2]*numColors
print("There are",row,"rows")
print("There are",col,"columns")
print("There are",numColors,"colors")
c=[]
for i in range(numColors):
    colorLine = fh.readline() 
    colorLine.strip()
    sym, c, color = colorLine.split()
    if(sym=="~"):
        sym=" "
    colorDefs[i][0] = sym
    colorDefs[i][1] = color
    #print(colorDefs[i][0],":",colorDefs[i][1])
    print(colorDefs)

x=0
if(row<=col):
    x=col
else:
    x=row
a=[0]*x
for i in range(x):
    turtle.penup()
    turtle.goto(x/2+i, x/2)
    turtle.pendown()
    turtle.dot(1,"blue")
    a[i]=fh.readline()
    print(a[i],end="")
print(colorDefs)
fh.close()
