def letterstonum(month):
    mnths = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    month=month.lower()
    for i in range(len(mnths)):
        if month==mnths[i]:
            month=i+1
    if int(month)<10:
        month="0"+str(month)
    return year+month+day

fh=open("wordle.dat","r")
for i in range(1038):
    read=fh.readline()
    read.strip()
    month,day,year,word=read.split()
print(letterstonum(month))

print("Welcome to the Wordle Database!")
x=input("Enter w if you are looking for a word, or d for a word on a certain date: ")
    