"""
Name: Humza Saleem Khan 
Student Number: 777320@pdsb.net
Course Code: ICS3U0
Assignment: Assignment 4 - Reading files and searching for data
12/19/2024

The header is located above including all the information

Variable Dictionary:
letters_to_num - Function that converts a date given as month, day, and year
  into a numerical string
month - Represents the month in a 3 letter abbreviation used to convert to a numerical format
day - Represents the day of the month used to include leading zeroes if needed
year - Represents the year and is combined with month and day to form a date string
mnths: Array of all 12 months as 3 letter abbreviations 
  which is used to find the numeric equivalent of the month
mergeSort - Function that sorts 2 arrays together using merge sort
merge - Function that merges two sorted sub-arrays back into the original arrays in sorted order
arr1 - Primary array of items to be sorted which holds values to be sorted like dates or words
arr2 - Secondary array that is sorted alongside arr1 which holds corresponding values to arr1
low - Starting index of the array segment to be processed which equals the 
  lower boundary in sorting or searching algorithms
high - Ending index of the array segment to be processed which equals the
  upper boundary in sorting or searching algorithms
-------------------------------------------------------------------------- 
mid - Middle index which is used to divide arrays into sub-arrays for 
  sorting or binary searching
i,j - General variables for iterating through arrays used in loops
n1 - Variable that stores the number of elements in the left sub-array
n2 - Variable that stores the number of elements in the right sub-array
L - Temporary array for the left sub-array from arr1 which holds
  elements from the left part of arr1 during merging
R - Temporary array for the right sub-array from arr1 which
  holds elements from the right part of arr1 during merging
L2 - Temporary array for the left sub-array from arr2 which
  holds elements from the left part of arr2 during merging
R2 - Temporary array for the right sub-array from arr2 which
  holds elements from the right part of arr2 during merging
input - Value being searched for in arr1 in isMatch function
isMatch - Function that searches for input in arr1 and returns the corresponding value from arr2
fh - variable for reading "wordle.dat"
int_arr - Array to store numerical versions of dates for comparison and sorting
word_arr - Array to store words from the file 
read - Variable that temporarily holds each line of text read from the file
on - Bool variable that controls the program's main loop
exit - String included in the user prompt to indicate the exit option
prompt - String to display options for the user to choose an action
search_by - User's input that determines whether the user wants to
  search by word or date or to exit the code
input_word - User's inputted word to search for in the database
date - Date when input_word word was the solution
yr - Year entered by the user
janToDec - Month abbreviation entered by the user
day_input - Day entered by the user 
int_date - Numerical string version of the entered date
wrd - Word corresponding to int_date
"""

#functions
def letters_to_num(month,day,year):
#declaring function letters_to_num that converts a date given as month, day, and year
#into a numerical string format
    mnths = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    #declare mnths array of all 12 months as 3 letter abbreviations
    month=month.lower()
    #convert month parameter into all lower case so its less case sensitive
    for i in range(len(mnths)):
    #for loop that goes through the mnths array
        if month==mnths[i]:
        #check if month taken as parameter is equal to the ith index of mnths
            month=str(i+1)
            #setting month to a numerical string based on the array mnths
    try:
    #declare try function
        if int(month)<10:
        #checks if the numerical month is less than 10 for formatting
            month="0"+str(month)
            #if month is less than 10 add a 0 to the beginning of the string
    except:
    #declaring except function incase month cannot be converted to int
        return 0
      #returns 0 to stop later returns and used as indicator in driver code
    return str(year+month+day)
    #returns the full date in a numerical string

def mergeSort(arr1,arr2, low, high):
#declaring function mergeSort that sorts 2 arrays together using merge sort
#takes 2 arrays and the upper and lower bounds of the processed array as parameters
    if low < high:
    #compares low and high to create an exit condition for the recursion
        mid = low + (high - low) // 2
        #calculating the middle index for splitting the array into sub-arrays for sorting
        mergeSort(arr1,arr2, low, mid)
        #sorting first half of array
        mergeSort(arr1,arr2, mid + 1, high)
        #sorting second half of array
        merge(arr1,arr2, low, mid, high)
        #merging the split arrays together by calling merge function
        
def merge(arr1,arr2, low, mid, high):
#declaring merge function that merges two sorted sub-arrays
#takes arr1 and arr2 along with the lower and upper bounds of the array and the middle
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
    
    #copying data to the temp arrays declared above
    for i in range(0, n1):
    #going through the left sub-array
        L[i] = arr1[low + i]
        #copying data 
        L2[i] = arr2[low + i]
        #copying data 
    for j in range(0, n2):
    #going through the right sub-array
        R[j] = arr1[mid + 1 + j]
        #copying data 
        R2[j] = arr2[mid + 1 + j]
        #copying data 
    #merging back the sub-arrays
    i = 0
    #setting i to 0 for merging left sub-array
    j = 0 
    #setting j to 0 for merging right sub-array
    k = low
    #setting k to the initial index of the merged sub-array
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr1[k] = L[i]
            arr2[k]=L2[i]
            i += 1
        else:
            arr1[k] = R[j]
            arr2[k] = R2[j]
            j += 1
        k += 1
    while i < n1:
        arr1[k] = L[i]
        arr2[k] = L2[i]
        i += 1
        k += 1
    while j < n2:
        arr1[k] = R[j]
        arr2[k] = R2[j]
        j += 1
        k += 1

def isMatch(input,arr1,arr2,low,high):
  if low>high:
    return 0  
  mid = low + (high - low) // 2
  if arr1[mid] == input:
    return arr2[mid]
  elif arr1[mid] < input:
    return isMatch(input,arr1,arr2,mid+1,high)
  else:
    return isMatch(input,arr1,arr2,low,mid-1) 
       
#main/driver code       
fh=open("wordle.dat","r")

int_arr=[]
word_arr=[]

for i in range(1038):
    read=fh.readline()
    read.strip()
    month,day,year,word=read.split()
    int_arr.append((letters_to_num(month,day,year)))
    word_arr.append(word)


print("Welcome to the Wordle Database!")
on = True
while on:
    
    exit=" or enter x to exit the program: "
    prompt="\nEnter w if you are looking for a word, or d for a word on a certain date"+exit
    search_by=input(prompt)
    
    if(search_by.lower()=='w'):
        mergeSort(word_arr,int_arr,0,len(word_arr)-1)
        input_word=input("What word are you looking for? ")
        input_word=input_word.upper()
        date=isMatch(input_word,word_arr,int_arr,0,len(word_arr)-1)
        if date != 0:
          print(f"The word {input_word} was the solution to the puzzle on {date}")
        else:
          print(f"{input_word} was not found in the database.")
          
    if(search_by.lower()=='d'):
        mergeSort(int_arr,word_arr,0,len(int_arr)-1)
        yr=(input("Enter the year: "))
        try:
            int(yr)
        except:
            print("Sorry this is not a valid input for the year please try again")
            continue 
        if(int(yr)<1):
            print("Sorry this is not a valid input for the year please try again")
            continue
        janToDec=(input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): "))
        day_input=(input("Enter the day: "))
        try:
            int(day_input)
        except:
            print("Sorry this is not a valid input for the day please try again")
            continue 
        if(int(day_input)<1):
            print("Sorry this is not a valid input for the day please try again")
            continue
        if int(day_input)<10:
          day_input="0"+day_input 
        int_date=letters_to_num(janToDec,day_input,yr)
        if(int_date == 0):
            print("Sorry you did not enter a valid month please try again")
            continue
        wrd=isMatch(int_date,int_arr,word_arr,0,len(int_arr)-1)
        if wrd != 0:
          print(f"The word entered on {int_date} was {wrd}")
        else:
          if(int(int_date)<20210619):
            print(f"{int_date} is too early. No wordles occurred before 20210619. Enter a later date.")
          if(int(int_date)>20240421):
            late_prmpt="Our records only go as late as 20240421. Please enter an earlier date."
            first=f"{int_date} is too recent. "+late_prmpt
            print(first)
            
    if(search_by.lower()=='x'):
      print("Thank you for using the Wordle Database good luck on future Wordles!")
      on=False
fh.close()
