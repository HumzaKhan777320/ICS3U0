ar2 = [[3, 4, 1, 2, 6], #creating a 2D array to later on add each element in each of the 3 1D arrays inside it
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
a=0# creating a variable to store the total value of each array
ar4=[]# new array to store each total value of the 3 arrays in the 2D array
for i in range(len(ar2)):#for loop to go through the 3 arrays in ar2
  ar3 = ar2[i]#storing each 1D array in in a new variable for simplicity
  for j in range(len(ar3)):#new for loop to go through each element in the 1D arrays
    a+=ar3[j]#adding the values of each element to the variable a to find the total of each array
  ar4.append(a)#appending the total value of each array to the empty array declared above
  a=0#setting a to 0 again for the next occurance of the loop
print(ar4)#after going throght the whole 2D array printing the new total array
