# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:08:55 2022

@author: rohan
"""
import requests

def saveFile(url):
    site=requests.get(url)
    filename=url.split('/')[-1]
    csv_file = open(filename, 'wb')
    
    csv_file.write(site.content)
    csv_file.close()
    return filename

fname=saveFile("https://sketchengine.co.uk/wp-content/uploads/word-list/english/english-word-list-total.csv")

print("The 20 top words in English:")

with open(fname,'r') as f:
    lines=f.readlines()[4:24]
    finalist=[(word[1].lower(),word[2]) for word in map(lambda x:x.split(';'), lines)]

    engTopWords=list(map(lambda x:x[0],finalist))
    for i,tup in enumerate(finalist):
        print(f"{i+1}. '{tup[0]}' ",end="")
        if tup!=finalist[-1]: print('- ',end="")
print()
print('-'*90)  

#Part b:
with open("TaleOfTwoCities.txt",'r') as f:
    S=f.readlines()[0]

#part c:
newS=list(filter(lambda x: x in engTopWords,S.split()))

print('-'*90)

#part d:
dic={}

for word in newS:
    if word in dic:
        dic[word]+=1
    else:
        dic[word]=1
print("All word frequencies from S Sorted:")
sortedS=sorted(dic,key=lambda x:dic[x],reverse=True)
print(sortedS)
print('-'*90)

#part e:
for rank,(engWord,Sword) in enumerate(zip(engTopWords,sortedS)):
    if engWord!=Sword:
        print(f"{rank+1}) English popular '{engWord}' is not the same rank as '{Sword}' from S")
    else:
        print(f"{rank+1}) English popular '{engWord}' is the same rank as '{Sword}' from S")
    
    
    
    