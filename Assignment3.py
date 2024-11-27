import turtle   

def plot(a,b,x,y,z,color,rotation):
    turtle.tracer(0,0)
    turtle.penup()
    x1=-a*z/4+(x*z/2)
    y1=b*z/4-(y*z/2)
    if(rotation == 0):
        turtle.goto(x1,y1)
    if(rotation == 90):
        turtle.goto(y1,-x1)
    if(rotation == 180):
        turtle.goto(-x1,-y1)
    if(rotation == 270):
        turtle.goto(-y1,x1)
    turtle.pendown()
    turtle.dot(z,color)
    turtle.hideturtle() 
      
def loops(fh,row,col,name_of_function,size,angle):
    a=[0]*row
    for j in range(row):
        a[j]=fh.readline()
        for t in range(col):
            for l in c1:
                if l[0]==a[j][t]:
                    k=l[1]
            name_of_function(row,col,t,j,size,k,angle)
    turtle.update()

prmpt="Enter the name of the file you would like displayed."
prmpt_continued=" Remeber it has to be in the same directory: "
whole_prmpt=prmpt+prmpt_continued
usr_inpt=input(whole_prmpt)

thickness=int(input("\nEnter the thickness: "))

angle1=int(input("What angle rotation do you want the image 0, 90, 180, or 270: "))
if(angle1 != 0):
    if(angle1 != 90):
        if(angle1 != 180):
           if(angle1 != 270): 
                print("Sorry this is not a valid angle so we'll default to 0")
                angle1=0
filename = usr_inpt
fh = open(filename, "r")

print("\nYour turtle window is now ready check your taskbar")

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

loops(fh,row,col,plot,thickness,angle1)        
fh.close()
turtle.mainloop()
