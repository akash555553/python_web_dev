#add lib that are required
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#get url
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# create a list for addition
s=list()
sum=0

#Retrieve all of the span tags... add content of span tag in list and get the sum
tags = soup('span')
for tag in tags:
    s.append(tag.contents[0])
    ii=int(tag.contents[0])
    sum=sum+ii
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
print(sum)
    #print('Attrs:', tag.attrs)
