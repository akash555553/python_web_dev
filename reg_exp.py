#import regular expretion lib
import re

#take file input   file name : regex_sum_1455060.txt
x=input("enter name of the file: ")

#open and read it
fh=open(x)
f=fh.read()

#use findall to extract specific info from text file with the help of regular expretion
y=re.findall('[0-9]+',f)

#print(y)
#make a list of numbers and get the sum of it &print it
s=list()
sum=0
for i in y:
    s.append(i)
    ii=int(i)
    sum=sum+ii

#print(s)
print(sum)
