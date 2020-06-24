fname = input("Enter file name: ")
fh = open(fname)
lst = list()
wds= list()
 
for line in fh:
	line=line.strip()
	wds=line.split()
	#print(wds)
	for word in wds:
		if word not in lst:
			lst.append(word)
lst.sort()
print(lst)
	
    
    
    
  
#print(wds)
#lst.sort()
