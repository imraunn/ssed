import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
import os


f=open("database.txt","r")
lines=f.read().splitlines()

data={}
for lang in lines:
    url="https://esolangs.org/wiki/"+str(lang)
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    for sample in soup.findAll(['pre','code']):
        print(urllib.parse.unquote(sample.text))
        print('\n')
        print(str(lang))
        print("-----------------------")
        val=input("Do you want to keep this? y/n ")
        if val=="y" :
            print("yos")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("gg")
            os.system('cls' if os.name == 'nt' else 'clear')
