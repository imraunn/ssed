import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
import os
import pprint


f=open("reduced_database.txt","r")
lines=f.read().splitlines()
syntax=["import","echo"]
data={}
for lang in lines:
    local={}
    url="https://esolangs.org/wiki/"+str(lang)
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    counter=1
    z=[]
    for sample in soup.findAll(['pre','code']):
        t=str(urllib.parse.unquote(sample.text)).replace("\n","")
        if len(t) > 10 and all(word not in t for word in syntax):
            z.append(t)
    if len(z)>=1:
        for j in z:
            print()
            print("Probable code ",counter)
            print("-----------------------")
            counter=counter+1
            print(j[:150])
            print("-----------------------")
        print()
        print("Language is", str(lang))
        val=input("What all do you want to keep? Enter values of counter as a string: ")
        m=1
        for i in val:
            local["code"+str(m)]=z[int(i)-1]
            m=m+1
        data[str(lang)]=local
        os.system('cls' if os.name == 'nt' else 'clear')

pprint.pprint(data)
#implement storage in a file using dictionary
