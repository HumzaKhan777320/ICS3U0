#not done yet
filename = "test.txt"
fh = open(filename, "r") 
numColors=3
colorDefs = [[0] * 2] * numColors 
for i in range(numColors):
   colorLine = fh.readline() 
   colorLine.strip()
   sym, c, color = colorLine.split()
   colorDefs[i][0] = sym
   colorDefs[i][1] = color
   if(sym=="~"):
       colorLine=colorLine.replace("~"," ")
   print(colorLine)
fh.close()
