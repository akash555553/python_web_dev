#import json urllib

import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#take json input
url = input('Enter json: ')
print('Retrieving', url)

#open and read using urllib
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())


#use json lib to load data into info
info = json.loads(data)
#print(info)

#put data into results which is inside comment area of json file
results=info["comments"]
#print('User count:', len(results))
#print(results)


#make a list to get count and sum from it
s=list()
for z in results:
    print(z["name"])
    print(z["count"])
    i=int(z["count"])
    s.append(i)


print(s)

#total count
sum=0
for z in s:
    sum=sum+z

print(sum)
