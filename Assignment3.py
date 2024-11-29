#Not even close to being done
"""
Name: Humza Saleem Khan
Student Number: 777320@pdsb.net
Course Code: ICS3U0
Assignment: Assignment 3 - Making a graphics plotter in Turtle
11/28/2024

Variable Dictionary:
inputs - Function to get user inputs and append to various_inputs array
prmpt - "Enter the name of the file you would like displayed."
prmpt_continued - " Remember it has to be in the same directory: "
whole_prmpt - Combined string of prmpt and prmpt_continued for input prompt
usr_inpt - User input for the filename
thickness - User input for the thickness of the plot
angle1 - User input for the angle rotation (0, 90, 180, 270)
various_inputs - Array to store user inputs (filename, thickness, angle1)
plot - Function to plot the turtle graphics based on coordinates, size, and color
row - Number of rows in the plot (from file)
col - Number of columns in the plot (from file)
x - Current x-coordinate in the plot loop
y - Current y-coordinate in the plot loop
size - Size of the dots to be plotted
color - Color of the dots to be plotted
angle - Rotation angle for the plot
fh - File handler for reading the input file
name_of_function - Variable holding the function to call for plotting
a - Array to store each row of the plot data
color_array - Function to read color definitions and call the plotting loop
colorDefs - 2D array to store symbol and color pairs
filtered_colorDefs - Filtered list of color definitions
numColors - Number of color definitions in the file
sym - Symbol for color definition
c - Character placeholder in color definition
colorLine - Line from file containing color information
"""
import turtle   

def inputs(various_inputs):    
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
    print("\nYour turtle window is now ready check your taskbar")
    various_inputs.append(usr_inpt)
    various_inputs.append(thickness)
    various_inputs.append(angle1)

def plot(row,col,x,y,size,color,angle):
    turtle.tracer(0,0)
    turtle.penup()
    x1=-row*size/4+(size*x/2)
    y1=col*size/4-(size*y/2)
    if(angle == 0):
        turtle.goto(x1,y1)
    if(angle == 90):
        turtle.goto(y1,-x1)
    if(angle == 180):
        turtle.goto(-x1,-y1)
    if(angle == 270):
        turtle.goto(-y1,x1)
    turtle.pendown()
    turtle.dot(size,color)
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

def color_array(colorDefs,filtered_colorDefs,numColors,fh,row,col,angle1,thickness):
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
    

various_inputs=[]  
inputs(various_inputs)
  
filename = various_inputs[0]
fh = open(filename, "r")
colorLine = fh.readline() 
colorLine.strip()
col = colorLine.split()[0]
row = colorLine.split()[1]
num = colorLine.split()[2]
row=int(row)
col=int(col)
numColors=int(num)
colorDefs = [[0]*2]*numColors
filtered_colorDefs=[[0]]*numColors
angle1=various_inputs[2]
thickness=various_inputs[1]
color_array(colorDefs,filtered_colorDefs,numColors,fh,row,col,angle1,thickness)
fh.close()
turtle.mainloop()

