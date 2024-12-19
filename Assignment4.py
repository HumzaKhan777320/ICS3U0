
#functions
def letters_to_num(month,day,year):
    mnths = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    month=month.lower()
    for i in range(len(mnths)):
        if month==mnths[i]:
            month=str(i+1)
    try:
        if int(month)<10:
            month="0"+str(month)
    except:
        return 0
    return str(year+month+day)

def mergeSort(arr1,arr2, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr1,arr2, l, m)
        mergeSort(arr1,arr2, m + 1, r)
        merge(arr1,arr2, l, m, r)
        
def merge(arr1,arr2, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    L2 = [0] * (n1)
    R2 = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr1[l + i]
        L2[i] = arr2[l + i]
    for j in range(0, n2):
        R[j] = arr1[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
    i = 0  
    j = 0 
    k = l 
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

def isMatch(y,arr1,arr2,low,high):
  if low>high:
    return 0  
  mid = low + (high - low) // 2
  if arr1[mid] == y:
    return arr2[mid]
  elif arr1[mid] < y:
    return isMatch(y,arr1,arr2,mid+1,high)
  else:
    return isMatch(y,arr1,arr2,low,mid-1) 
       
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
    x=input(prompt)
    
    if(x.lower()=='w'):
        mergeSort(word_arr,int_arr,0,len(word_arr)-1)
        y=input("What word are you looking for? ")
        y=y.upper()
        date=isMatch(y,word_arr,int_arr,0,len(word_arr)-1)
        if date != 0:
          print(f"The word {y} was the solution to the puzzle on {date}")
        else:
          print(f"{y} was not found in the database.")
          
    if(x.lower()=='d'):
        
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
            
    if(x.lower()=='x'):
      print("Thank you for using the Wordle Database good luck on future wordles!")
      on=False
fh.close()
