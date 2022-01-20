#import required lib

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#take xml input
url = input('Enter xml: ')
print('Retrieving', url)

#open and read using urllib
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())

#use xml ET.fromstring to parse xml data
commentinfo = ET.fromstring(data)

#by using findall get only data which is inside"comments/comment"
results =commentinfo.findall('comments/comment')
print("User count",len(results))

#make a list to put req data for addition
s=list()
for item in results:
    print("name" ,item.find('name').text)
    print("count" ,item.find('count').text)
    
    i=int(item.find('count').text)
    s.append(i)

print(s)
#total count
sum=0
for z in s:
    sum=sum+z

print(sum)
