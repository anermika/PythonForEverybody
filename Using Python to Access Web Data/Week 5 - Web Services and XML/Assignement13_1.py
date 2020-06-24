import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
tree=ET.fromstring(html)
lst=tree.findall('comments/comment')
sum=0
for item in lst:
    #print('Name', item.find('name').text)
    #print('Count',item.find('count').text)
    count=int(item.find('count').text)
    sum=sum+count
print(sum)
