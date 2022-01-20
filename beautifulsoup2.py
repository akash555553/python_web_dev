#retrive required lib

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# take input url
url = input('Enter - ')


#create while loop to repeat the process 7 times
c=7
while c>0:
    c=c-1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # make 2 lists for names and links
    name=list()
    link=list()

    #Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        #print(tag.get('href', None))
        #print('Contents:', tag.contents[0])
        name.append(tag.contents[0])
        link.append(tag.get('href', None))

    #put url value of 18th link
    url=link[17]
    print(name[17])
    #print(link[17])

    #clr list to we can use this in next loop
    name.clear()
    link.clear()
