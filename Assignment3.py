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
whole_prmpt - Combined string of prmpt and prmpt_continued for the file name input
usr_inpt - User input for the filename
thickness - User input for the thickness/size of the image
angle1 - User input for the angle rotation (0, 90, 180, 270)
various_inputs - Array to store user inputs (filename, thickness, angle1)
plot - Function to plot the image based on coordinates, size, and color
row - Number of rows in the image (from file)
col - Number of columns in the image (from file)
x - Current x coordinate being plotted
y - Current y coordinate being plotted
size - Size of the dots to be plotted (same as thickness)
color - Color of the dots to be plotted
angle - Rotation angle for plotting
fh - Variable for oppening the file 
loops - Function to go through each symbol/pixel in the image (from file) and find its
    corresponding color information (from file) and call the plot function
temp_array - Array to store each row of the plot data
color_array - Function to read color information and store it
colorDefs - 2D array to store symbol and color pairs
filtered_colorDefs - Filtered list of color definitions
current_color_line - Variable to hold a color definition to compare against a symbol in
    the encoded image (from file)
numColors - Number of color definitions in the file
sym - Variable that stores a symbol corrisponding with a color code
c - Variable needed for unpacking color definitions
colorLine - Variable that stores a line from the file containing color information
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
    thickness=int(input("\nEnter the desired thickness of the image as an integer >1: "))
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

def color_array(numColors,colorDefs,filtered_colorDefs):
    #declaring color_array function to read color information and store it
    for i in range(numColors):
        #going through each color definition in inputted file
        colorLine = fh.readline()
        #storing line of color data in variable colorLine  
        colorLine.strip()
        #getting rid of unwanted space in data line
        sym, c, color = colorLine.split()
        #unpacking the line of color data into 3 variables
        if(sym=="~"):
            #checking if a symbol for color definition is a '~'
            sym=" "
            #changing that symbol to a " "(space)
        colorDefs[i][0] = sym
        #storing a symbol for color definition in colorDefs array
        colorDefs[i][1] = color
        #storing coresponding color code for color definition in colorDefs array
        filtered_colorDefs[i]=[colorDefs[i][0],colorDefs[i][1]]
        #storing pairs of corresponding color information in a new focused array
        #filtered_colorDefs


def loops(row,col,size,angle,filtered_colorDefs):
    #Function to go through each symbol/pixel in the image (from file) and find its
    #corresponding color information (from file)
    #taking the number of rows and columns in the image, the size of each dot, 
    # the angle of rotation and the list of color definitions as parameters 
    temp_array=[0]*row
    #creating a temporary array of size row to append each line of the encoded image
    for y in range(row):
        #goes through each element in the temp_array
        #to read through each line of the image (from file)
        temp_array[y]=fh.readline()
        #store the y+1th line of the image encoded at the yth index of temp_array
        for x in range(col):
            #for loop to go through each symbol in each line of image/plotting data
            for j in range (len(filtered_colorDefs)):
                #for loop to go through the list of color definitions to 
                #find the correct corresponding color
                current_color_line=filtered_colorDefs[j]
                #storing the jth index of filtered_colorDefs in current_color_line
                #to check if the symbol coresponds with it
                if current_color_line[0]==temp_array[y][x]:
                    #comparing the curent symbol to a color definition
                    color=current_color_line[1]
                    #creating variable color and setting it to the color based
                    #on the symbol
            plot(x,y,size,color,angle)
            #calling the plot function with the x and y values along with the
            #color and angle of rotation
    turtle.update()
    #updating the turtle screen 
    #needed due to turtle.tracer() located in the plot function

def plot(x,y,size,color,angle):
    #function to plot a point on the turtle screen at a certain coordenate and of a certain size/color
    #and rotation
    #takes ints x and y as parameters toi find the location of plotting
    #takes int size and string color to plot the point of desired size and color
    #takes int angle to alter the images rotation
    turtle.tracer(0,0)
    #hides the turtle while plotting for faster plotting
    turtle.penup()
    #lifts the turtle pen to move it to a certain location
    x1=-col*(size/4)+(x*size/2)
    y1=row*(size/4)-(y*size/2)
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
color_array(numColors,colorDefs,filtered_colorDefs)
loops(row,col,thickness,angle1,filtered_colorDefs)
fh.close()
turtle.mainloop()
