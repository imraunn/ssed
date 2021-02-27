import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
import os


f=open("database.txt","r")
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
            """print(urllib.parse.unquote(sample.text))
            print('\n')
            print(str(lang))
            print("-----------------------")"""
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
        for i in val:
            local["code"+str(i)]=z[int(i)-1]
        print(local)
            #implement storage in a file using dictionary


    """
            val=input("Do you want to keep this? y/n ")
            if val=="y" :
                print("yos")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("gg")
                os.system('cls' if os.name == 'nt' else 'clear')
    """
