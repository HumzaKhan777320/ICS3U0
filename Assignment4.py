def letterstonum():
    mnths = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    for i in range(len(mnths)):
        if month=mnths[i]:
            month=i+1


fh=open("wordle.dat","r")
for i in range(1038):
    read=fh.readline()
    read.strip()
    month,day,year,word=read.split()
    
