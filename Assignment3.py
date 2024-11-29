#Not even close to being done
"""
Name: Humza Saleem Khan
Student Number: 777320@pdsb.net
Course Code: ICS3U0
Assignment: Assignment 3 - Making a graphics plotter in Turtle
11/28/2024

Variable Dictionary:
inputs - Function to get user inputs and append to various_inputs array
prmpt - First part of user prompt
prmpt_continued - Second part of user prompt
whole_prmpt - Combined string of prmpt and prmpt_continued for input prompt
usr_inpt - User input for the filename
thickness - User input for the thickness of the plot
angle1 - User input for the angle rotation (0, 90, 180, 270)
various_inputs - Array to store user inputs (filename, thickness, angle1)
plot - Function to plot the turtle graphics based on coordinates, size, and color
row - Number of rows in the plot (from file)
col - Number of columns in the plot (from file)
x - Current x coordinate being plotted
y - Current y coordinate being plotted
size - Size of the dots to be plotted
color - Color of the dots to be plotted
angle - Rotation angle for plotting
fh - Variable for oppening abd holding the file 
name_of_function - Variable holding the function to call for plotting
temp_array - Array to store each row of the plot data
color_array - Function to read color definitions and call the loops function
colorDefs - 2D array to store symbol and color pairs
filtered_colorDefs - Filtered list of color definitions
numColors - Number of color definitions in the file
sym - Symbol for color definition
c - Character placeholder in color definition
colorLine - Line from file containing color information
"""
import turtle   
# importting turtle library
def inputs(various_inputs):
    #defining inputs function with various_inputs array as parameter    
    prmpt="Enter the name of the file you would like displayed."
    #first part of the user's prompt for file name
    prmpt_continued=" Remeber it has to be in the same directory: "
    #second part of the user's input for file name
    whole_prmpt=prmpt+prmpt_continued
    # compining the 2 parts into one prompt
    usr_inpt=input(whole_prmpt)
    #displaying prompt to user
    #taking the file name as input from the user and storing in usr_inpt
    thickness=int(input("\nEnter the thickness: "))
    #taking user input for the thichness of each point (size of image)
    angle1=int(input("What angle rotation do you want the image 0, 90, 180, or 270: "))
    #taking the angle of rotation from the user with provided prompt
    if(angle1 != 0): #checking if the angle is not 0
        if(angle1 != 90):#checking if thae angle is not 90
            if(angle1 != 180):#checking if the angle is not 180
                if(angle1 != 270): #checking if the angle is not 270
                    print("Sorry this is not a valid angle so we'll default to 0")
                    #telling the user they did not input a valid angle
                    angle1=0
                    #defaulting to a 0 degree angle
    print("\nYour turtle window is now ready check your taskbar")
    #telling the user to check for the turtle window
    various_inputs.append(usr_inpt)
    #appending inputed file name to various_inputs array for out of function access
    various_inputs.append(thickness)
    #appending inputed thickness to various_inputs array for out of function access
    various_inputs.append(angle1)
    #appending inputed angle to various_inputs array for out of functiopn access

def color_array(colorDefs,filtered_colorDefs,numColors,fh,row,col,angle1,thickness):
    #declaring
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


def loops(fh,row,col,name_of_function,size,angle):
    temp_array=[0]*row
    for y in range(row):
        temp_array[y]=fh.readline()
        for x in range(col):
            for i in filtered_colorDefs:
                if i[0]==temp_array[y][x]:
                    color=i[1]
            name_of_function(row,col,x,y,size,color,angle)
    turtle.update()

def plot(row,col,x,y,size,color,angle):
    turtle.tracer(0,0)
    turtle.penup()
    x1=-row*1.25*size/4+(size*x/1.5)
    y1=col*1.5*size/4-(size*y/1.5)
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
turtle.screensize(400,400,"gray") 
color_array(colorDefs,filtered_colorDefs,numColors,fh,row,col,angle1,thickness)
fh.close()
turtle.mainloop()
