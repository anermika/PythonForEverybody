# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos1=line.find(':')
    num=line[pos1+1:]
    numb=(float(num))
    total = total + numb
    count=count+1

final= total/float(count)
print ("Average spam confidence:", final) 
    

