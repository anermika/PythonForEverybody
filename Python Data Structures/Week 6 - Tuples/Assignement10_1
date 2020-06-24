name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
lst=list()
for line in handle:
    if not line.startswith('From '): continue
    words=line.split()
    #print(words)
    time=words[5]
    #print(time)
    hours=time.split(':')
    hours=hours[0]
    #print(hours)
    counts[hours]=counts.get(hours,0)+1

#print(counts)
lst=sorted(counts.items())
#print(lst)
for v,k in lst:
	print(v,k)
