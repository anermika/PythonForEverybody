hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate:")
r = float(rte)
if hrs > 40:
    pay = (h - 40) * (r * 1.5) + (40 * r)
else:
	pay = (h * r)
print(pay)
