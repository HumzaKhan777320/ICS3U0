#Not done yet
"""
Name: Humza Saleem Khan 
Student Number: 777320@pdsb.net
Course Code: ICS3U0
Assignment: FINAL PROJECT - Credit Card Report
01/15/2025


Variable Dictionary:

"""

#functions
def date(month,year):
    month=int(month)
    year=int(year)
    if month<10:
        month="0"+str(month)
    year=str(year)
    month=str(month)
    temp=str(year+month)
    temp=int(temp)
    return(temp)
#----------------------------------------------------------------------------------------------------------------
def mergeSort(arr1,arr2,arr3,arr4,arr5, low, high):
#declaring function mergeSort that sorts arr1 and changes arr2-5 accordingly using merge sort
#takes 5 arrays and the upper and lower bounds of the processed array as parameters
    if low < high:
    #compares low and high to create an exit condition for the recursion
        mid = low + (high - low) // 2
        #calculating the middle index for splitting the array into sub-arrays for sorting
        mergeSort(arr1,arr2,arr3,arr4,arr5, low, mid)
        #sorting first half of array
        mergeSort(arr1,arr2,arr3,arr4,arr5, mid + 1, high)
        #sorting second half of array
        merge(arr1,arr2,arr3,arr4,arr5, low, mid, high)
        #merging the split arrays together by calling merge function
        
def merge(arr1,arr2,arr3,arr4,arr5, low, mid, high):
#declaring merge function that merges two sorted sub-arrays
#takes arr1-5 along with the lower and upper bounds of the array and the middle
#index as parameters
    n1 = mid - low + 1
    #calculate the number of elements in the left sub-array and store in n1
    n2 = high - mid
    #calculate the number of elements in the right sub-array and store in n2
    L = [0] * (n1)
    #creating temp arrays
    R = [0] * (n2)
    #creating temp arrays
    L2 = [0] * (n1)
    #creating temp arrays
    R2 = [0] * (n2)
    #creating temp arrays
    L3 = [0] * (n1)
    #creating temp arrays
    R3 = [0] * (n2)
    #creating temp arrays
    L4 = [0] * (n1)
    #creating temp arrays
    R4 = [0] * (n2)
    #creating temp arrays
    L5 = [0] * (n1)
    #creating temp arrays
    R5 = [0] * (n2)
    #creating temp arrays
    
    #copying data to the temp arrays declared above
    for i in range(0, n1):
    #going through the left sub-array
        L[i] = arr1[low + i]
        #copying data 
        L2[i] = arr2[low + i]
        #copying data
        L3[i] = arr3[low + i]
        #copying data
        L4[i] = arr4[low + i]
        #copying data
        L5[i] = arr5[low + i]
        #copying data 
    for j in range(0, n2):
    #going through the right sub-array
        R[j] = arr1[mid + 1 + j]
        #copying data 
        R2[j] = arr2[mid + 1 + j]
        #copying data
        R3[j] = arr3[mid + 1 + j]
        #copying data 
        R4[j] = arr4[mid + 1 + j]
        #copying data
        R5[j] = arr5[mid + 1 + j]
        #copying data 

    #merging back the sub-arrays
    i = 0
    #setting i to 0 for merging left sub-array
    j = 0 
    #setting j to 0 for merging right sub-array
    k = low
    #setting k to the initial index of the merged sub-array
    while i < n1 and j < n2:
    #checking if either sub-array has been completed yet
        if L[i] <= R[j]:
        #comparingeach sub-arrays corresponding elements
            arr1[k] = L[i]
            #copying the data from left sub-array back to it's main array
            arr2[k]=L2[i]
            #copying the data from left sub-array back to it's main array
            arr3[k]=L3[i]
            #copying the data from left sub-array back to it's main array
            arr4[k]=L4[i]
            #copying the data from left sub-array back to it's main array
            arr5[k]=L5[i]
            #copying the data from left sub-array back to it's main array
            i += 1
            #incrementing i and not j since the jth index of R-R5 wasnt copyed yet
        else:
        #declaring else statment
            arr1[k] = R[j]
            #copying the data from right sub-array back to it's main array
            arr2[k] = R2[j]
            #copying the data from right sub-array back to it's main array
            arr3[k] = R3[j]
            #copying the data from right sub-array back to it's main array
            arr4[k] = R4[j]
            #copying the data from right sub-array back to it's main array
            arr5[k] = R5[j]
            #copying the data from right sub-array back to it's main array
            j += 1
            #incrementing j and not i since the ith index of L-L5 wasnt copyed yet
        k += 1
        #adding to k so we don't change the same index of the merged array twice
    while i < n1:
    #checking if there's anything left in L-L5 that wasn't copied
        arr1[k] = L[i]
        #adding anything left in L to it's main array
        arr2[k] = L2[i]
        #adding anything left in L2 to it's main array
        arr3[k] = L3[i]
        #adding anything left in L3 to it's main array
        arr4[k] = L4[i]
        #adding anything left in L4 to it's main array
        arr5[k] = L5[i]
        #adding anything left in L5 to it's main array
        i += 1
        #incrementing i since the ith index has now been copied 
        k += 1
        #incrementing k since the ith index has now been copied to
        # the kth index of the merged arrays 
    while j < n2:
    #checking if there's anything left in R-R5 that wasn't copied
        arr1[k] = R[j]
        #adding anything left in R to it's main array
        arr2[k] = R2[j]
        #adding anything left in R2 to it's main array
        arr3[k] = R3[j]
        #adding anything left in R3 to it's main array
        arr4[k] = R4[j]
        #adding anything left in R4 to it's main array
        arr5[k] = R5[j]
        #adding anything left in R5 to it's main array
        j += 1
        #incrementing j since the jth index has now been copied 
        k += 1
        #incrementing k since the jth index has now been copied to 
        # the kth index of the merged arrays 



file=True
#creating bool variable file and setting to true to check if "data.dat" is on the user's computer
try:
#declaring try function
  fh=open("data.dat","r")
  #opening the "data.dat" file for reading
except:
#declaring except function
  file=False
  #setting file to False to stop further code
if file==True:
#checks if file is true
    first_name=[]
    #declaring array to store each first name
    last_name=[]
    #declaring array to store each last name
    cctype=[]
    #declaring array to store each type of card
    ccNumber=[]
    #declaring array to store each credit card number
    wholeExp=[]
    #declaring array to store each full expiary number
    temp_line=fh.readline()
    #reading the first line of the file outside of loop because it dose not have valid information
    for i in range(200):
    #creating a for loop to go through each line of the file
        read=fh.readline()
        #reading the ith line of the file and storing in read
        read.strip()
        #removing whitespace in between characters
        name,lastname,type,number,month,year = read.split(',')
        #spliting the line of data into each piece of data
        wholeExp.append(date(month,year))
        #calling the date function with the month and year of expiary and storing to wholeExp 
        first_name.append(name)
        #appending the first name in the current line of data to first_name array
        last_name.append(lastname)
        #appending the last name in the current line of data to last_name array
        cctype.append(type)
        #appending the credit card type in the current line of data to cctype array
        ccNumber.append(number)
        #appending the credit card number in the current line of data to ccNumber array
    fh.close()
    #closing the file to prevent corruption          


    mergeSort(wholeExp,ccNumber,cctype,last_name,first_name,0,len(wholeExp)-1)
    #calling mergeSort function which sorts based on the expiary date
    Write=open("credit_card-report.txt","w")
    #opening/creating the credit_card-report function for writing and storing in access variable Write
    for i in range(len(wholeExp)):#----------------------------------------------------------------------------------------------------------------
        if wholeExp[i]<202501:
            Write.write("%-38s %-13s #%s %d EPIRED \n" %((first_name[i]+" "+last_name[i]+":"), cctype[i], ccNumber[i], wholeExp[i]))
        elif wholeExp[i]==202501:
            Write.write("%-38s %-13s #%s %d RENEW IMMEDIATELY\n" %((first_name[i]+" "+last_name[i]+":"), cctype[i], ccNumber[i], wholeExp[i]))


    Write.close()
    print("Thank you for using the Credit Card Report Program your report is located in the file credit_card-report.txt on your computer.")

             

else:
#declaring else statement 
  print("Sorry the data file data.dat was not found in the right directory check the file and try again")
  #telling the user the "data.dat" file was not found and to try the code again after checking file
