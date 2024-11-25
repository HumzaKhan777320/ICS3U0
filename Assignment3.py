import turtle   

def plot(a,b,x,y,z,color):
    turtle.tracer(0,0)
    turtle.penup()
    turtle.goto(-a*2/2+(x*2),b*2/2-(y*2))
    turtle.pendown()
    turtle.dot(z,color)
    turtle.hideturtle()
    
def flip(a,b,x,y,z,color):
    turtle.tracer(0,0)
    turtle.penup()
    turtle.goto(a*2/2-(x*2),-b*2/2+(y*2))
    turtle.pendown()
    turtle.dot(z,color)
    turtle.hideturtle() 
      
def q(fh,row,col,z):
    a=[0]*row
    for j in range(row):
        a[j]=fh.readline()
        for t in range(col):
            for l in c1:
                if l[0]==a[j][t]:
                    k=l[1]
            z(row,col,t,j,3,k)
    turtle.update()

prmpt="Enter the name of the file you would like displayed."
prmpt_continued=" Remeber it has to be in the same directory: "
whole_prmpt=prmpt+prmpt_continued
usr_inpt=input(whole_prmpt)
filename = usr_inpt
fh = open(filename, "r")

colorLine = fh.readline() 
colorLine.strip()
col, row, num = colorLine.split()

row=int(row)
col=int(col)
numColors=int(num)

colorDefs = [[0]*2]*numColors
c1=[[0]]*numColors

for i in range(numColors):
    colorLine = fh.readline() 
    colorLine.strip()
    sym, c, color = colorLine.split()
    if(sym=="~"):
        sym=" "
    colorDefs[i][0] = sym
    colorDefs[i][1] = color
    c1[i]=[colorDefs[i][0],colorDefs[i][1]]

q(fh,row,col,plot)        
fh.close()
turtle.mainloop()

