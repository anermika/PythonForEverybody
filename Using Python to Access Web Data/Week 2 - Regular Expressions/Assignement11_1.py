handle = open('regex_sum_381508.txt')
import re
sum=0
for line in handle:
#print(line)
    num=re.findall('[0-9]+', line)
    print(num)
    for n in num:
        sum=sum+float(n)
print(sum)
