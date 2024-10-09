def comp(S):#defining a function that takes parameter S
  z=""#creating an empty string to store the output
  for i in range(len(S)):
    if(S[i]=="A"):
      x.append("T")
    if(S[i]=="T"):
      x.append("A")
    if(S[i]=="C"):
      x.append("G")
    if(S[i]=="G"):
      x.append("C")
    z=z+x[i]
  return(z)
  

x=[] 
y=input("Enter DNA strand")
print(comp(y))
