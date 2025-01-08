#not close to being done
def date(month,year):
    if int(month)<10:
        month="0"+str(month)
    return str(year+month)


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
    #checking if either sub-array has been completed yet
        if L[i] <= R[j]:
        #comparingeach sub-arrays corresponding elements
            arr1[k] = L[i]
            #copying the data from left sub-array back to the main array
            arr2[k]=L2[i]
            #copying the data from left sub-array back to the main array
            i += 1
            #incrementing i and not j since the jth index of R/R2 wasnt copyed yet
        else:
        #declaring else statment
            arr1[k] = R[j]
            #copying the data from right sub-array back to the main array
            arr2[k] = R2[j]
            #copying the data from right sub-array back to the main array
            j += 1
            #incrementing j and not i since the ith index of L/L2 wasnt copyed yet
        k += 1
        #adding to k so we don't change the same index of the merged array twice
    while i < n1:
    #checking if there's anything left in L/L2 that wasn't copied
        arr1[k] = L[i]
        #adding anything left in L to the main array
        arr2[k] = L2[i]
        #adding anything left in L2 to the secondary array
        i += 1
        #incrementing i since the ith index has now been copied 
        k += 1
        #incrementing k since the ith index has now been copied to
        # the kth index of the merged arrays 
    while j < n2:
    #checking if there's anything left in R/R2 that wasn't copied
        arr1[k] = R[j]
        #adding anything left in R to the main array
        arr2[k] = R2[j]
        #adding anything left in R2 to the secondary array
        j += 1
        #incrementing j since the jth index has now been copied 
        k += 1
        #incrementing k since the jth index has now been copied to 
        # the kth index of the merged arrays 
def isMatch(input,arr1,arr2,low,high):
#function for checking if input occurs in arr 1 and
#returns the corresponding value in arr2
  if low>high:
  #checks if lower bound of arr1 is higher then the upper bound
    return 0  
    #returns 0 as an indicator that input is not located in arr1
  mid = low + (high - low) // 2
  #calculating the middle index for spliting the array when searching 
  #through recursion
  if arr1[mid] == input:
  #checks if the mid index of arr1 equals input
    return arr2[mid]
    #returns the corresponding value of arr2
  elif arr1[mid] < input:
  #checks if mid is to low index
    return isMatch(input,arr1,arr2,mid+1,high)
    #calls isMatch again with a higher low parameter
  else:
  #declaring else statment
    return isMatch(input,arr1,arr2,low,mid-1) 
    #calls isMatch again with a lower high parameter
       

file=True
try:     
  fh=open("data.dat","r")
except:
  file=False
if file==True:
  first_name=[] 
  last_name=[]
  cctype=[]
  ccNumber=[]
  wholeExp=[]
temp_line=fh.readline()

  for i in range(200):
      read=fh.readline()
      name,lastname,type,number,month,year = read.split(',')
      wholeExp.append(date(month,year))
      word_arr.append(word)
      #storing each word into the word_arr array


  print("Welcome to the Wordle Database!")
  #printing a message to the user welcoming them
  on = True
  #declaring bool variable on and setting to true
  while on:
  #declariong while loop that works if on is true
      exit=" or enter x to exit the program: "
      #declaring string included in the user prompt to indicate the exit option
      prompt="\nEnter w if you are looking for a word, or d for a word on a certain date"+exit
      #declaring string to display options for the user to choose an action
      search_by=input(prompt)
      #displaying the prompt to the user and taking input to store in search_by
      if(search_by.lower()=='w'):
      #check if the user inputted w
          mergeSort(word_arr,int_arr,0,len(word_arr)-1)
          #calling mergeSort function to sort the word_arr
          input_word=input("What word are you looking for? ")
          #asking the user to input the word they are looking for and storing in input
          input_word=input_word.upper()
          #capitalizing the user's inputted word to compare to in isMatch
          date=isMatch(input_word,word_arr,int_arr,0,len(word_arr)-1)
          #calling isMatch function with input_word as the word to be searched for
          #and storing the return (corresponding date) in date
          if date != 0:
          #checks if the return is not 0
            print(f"The word {input_word} was the solution to the puzzle on {date}")
            #tells the user what date the entered word was for
          else:
            print(f"{input_word} was not found in the database.")
            #tells the user that there inputted word was not found
            
      if(search_by.lower()=='d'):
      #check if the user inputted d
          mergeSort(int_arr,word_arr,0,len(int_arr)-1)
          #calling mergeSort function to sort the int_arr
          yr=(input("Enter the year: "))
          #soring the users inputted year in yr
          try:
          #declaring try function
              int(yr)
              #trying to covnert yr to type int to see if its valid
          except:
          #declaring except function
              print("Sorry this is not a valid input for the year please try again")
              #telling the user there input for year is invalid and to try again
              continue 
              #ending this run of the loop and starting the loop again 
          if(int(yr)<1):
          #checking that the user's input for the year is positive
              print("Sorry this is not a valid input for the year please try again")
              #telling the user there input for year is invalid and to try again
              continue
              #ending this run of the loop and starting the loop again 
          janToDec=(input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): "))
          #asking the usr to input the month they are loking for in a 3 letter abriviation
          #and storing in jantoDec
          day_input=(input("Enter the day: "))
          #asking the usr to input the day they are loking for and storing in day_input
          try:
          #declaring try function
              int(day_input)
              #trying to convert day_input to int to check it is a valid input
          except:
          #declaring except function
              print("Sorry this is not a valid input for the day please try again")
              #telling the user there input for day is invalid and to try again
              continue 
              #ending this run of the loop and starting the loop again 
          if(int(day_input)<1):
              print("Sorry this is not a valid input for the day please try again")
              #telling the user there input for day is invalid and to try again
              continue
              #ending this run of the loop and starting the loop again 
          if int(day_input)<10:
          #checking if the day the user entered is less than 10
            day_input="0"+day_input 
            #adding a 0 to the day the user inputted for comparing the larger int
          int_date=letters_to_num(janToDec,day_input,yr)
          #calling the letters_to_num function with the user's inputed date and
          #storing the return in int_date
          if(int_date == 0):
          #checking if the letters_to_num function returned 0 indicating 
          #the user did not input a valid month
              print("Sorry you did not enter a valid month please try again")
              #telling the user there input for month is invalid and to try again
              continue
              #ending this run of the loop and starting the loop again 
          wrd=isMatch(int_date,int_arr,word_arr,0,len(int_arr)-1)
          #calling the isMatch function with the user's inputted date
          #as the date to search for
          if wrd != 0:
          #checking if the isMatch function dosn't return 0
            print(f"The word entered on {int_date} was {wrd}")
            #telling the user what word was entered on the inputted date
          else:
          #declaring else statment
            if(int(int_date)<20210619):
            #checking if the inputed date is too early
              print(f"{int_date} is too early. No wordles occurred before 20210619. Enter a later date.")
              #telling the user there input is too early
            if(int(int_date)>20240421):
            #checking if the inputed date is too late
              late_prmpt="Our records only go as late as 20240421. Please enter an earlier date."
              # second part of string telling the user there input is too late
              first=f"{int_date} is too recent. "+late_prmpt
              #whole string telling the user there input is too late
              print(first)
              #outputting whole string telling the user there input is too late
      if(search_by.lower()=='x'):
      #checking if the user enterd an x
        print("Thank you for using the Wordle Database good luck on future Wordles!")
        #thanking the user for using the code
        on=False
        #setting the on variable to false to end the loop
  fh.close()
  #closing the file to prevent corruption
else:
#declaring else statement 
  print("Sorry the data file wordle.dat was not found in the right directory check the file and try again")
  #telling the user the "wordle.dat" file was not found and to try the code again after checking file
