def computepay(h,r):
	if h>40:
		p = (h-40)*(r*1.5)+(40*r)
	else:
		p = (h*r)
	return print ("Pay" ,p)

hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate:")
r = float(rte)
computepay(h,r)

