#Not even close to being done
"""
Name: Humza Khan
Student Number: 777320@pdsb.net
Course Code: ICS3U0
Assignment: Assignment 3 - Making a graphics plotter in Turtle
11/27/2024

Variable Dictionary:

"""
import turtle   

def plot(row,col,x,y,size,color,angle):
    turtle.tracer(0,0)
    turtle.penup()
    turtle.shape("square")
    x1=-row*size/4+(size*x/2)
    y1=col*size/4-(size*y/2)
    if(angle == 0):
        turtle.goto(x1*2,y1*2)
    if(angle == 90):
        turtle.goto(y1,-x1)
    if(angle == 180):
        turtle.goto(-x1,-y1)
    if(angle == 270):
        turtle.goto(-y1,x1)
    turtle.pendown()
    turtle.color(color)
    turtle.turtlesize(size,size)
    turtle.stamp()
    turtle.hideturtle() 
      
def loops(fh,row,col,name_of_function,size,angle):
    a=[0]*row
    for y in range(row):
        a[y]=fh.readline()
        for x in range(col):
            for i in filtered_colorDefs:
                if i[0]==a[y][x]:
                    color=i[1]
            name_of_function(row,col,x,y,size,color,angle)
    turtle.update()


prmpt="Enter the name of the file you would like displayed."
prmpt_continued=" Remeber it has to be in the same directory: "
whole_prmpt=prmpt+prmpt_continued

usr_inpt=input(whole_prmpt)
filename = usr_inpt
fh = open(filename, "r")

thickness=int(input("\nEnter the thickness: "))

angle1=int(input("What angle rotation do you want the image 0, 90, 180, or 270: "))

if(angle1 != 0):
    if(angle1 != 90):
        if(angle1 != 180):
           if(angle1 != 270): 
                print("Sorry this is not a valid angle so we'll default to 0")
                angle1=0



print("\nYour turtle window is now ready check your taskbar")

colorLine = fh.readline() 
colorLine.strip()
col, row, num = colorLine.split()

row=int(row)
col=int(col)
numColors=int(num)

colorDefs = [[0]*2]*numColors
filtered_colorDefs=[[0]]*numColors

for i in range(numColors):
    colorLine = fh.readline() 
    colorLine.strip()
    sym, c, color = colorLine.split()
    if(sym=="~"):
        sym=" "
    colorDefs[i][0] = sym
    colorDefs[i][1] = color
    filtered_colorDefs[i]=[colorDefs[i][0],colorDefs[i][1]]

loops(fh,row,col,plot,thickness,angle1)

fh.close()
turtle.mainloop()

