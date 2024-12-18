def letters_to_num(month):
    mnths = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    month=month.lower()
    for i in range(len(mnths)):
        if month==mnths[i]:
            month=str(i+1)
    if int(month)<10:
        month="0"+str(month)
    return year+month+day

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
       
       
fh=open("wordle.dat","r")

int_arr=[]
word_arr=[]

for i in range(1038):
    read=fh.readline()
    read.strip()
    month,day,year,word=read.split()
    int_arr.append(int(letters_to_num(month)))
    word_arr.append(word)

print("Welcome to the Wordle Database!")
boolean_x = True
while boolean_x:
    x=input("Enter w if you are looking for a word, or d for a word on a certain date: ")
    if(x.lower()=='w'):
        mergeSort(word_arr,int_arr,0,len(word_arr)-1)
    if(x.lower()=='d'):
        mergeSort(int_arr,word_arr,0,len(int_arr)-1)
