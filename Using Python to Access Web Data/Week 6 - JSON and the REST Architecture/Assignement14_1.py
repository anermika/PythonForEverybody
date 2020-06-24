import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(html)
print('User count:', len(info))
#print(info)
sum=0
for item in info['comments']:
    #print('Name', item['name'])
    #print('Count', item['count'])
    counts=('Count', item['count'])
    #print(counts[1])
    count=(counts[1])
    sum=sum+count
print(sum)
