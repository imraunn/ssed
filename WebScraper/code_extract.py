import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
import os
import pprint
import sys


f=open("./storage/reduced_database.txt","r")
lines=f.read().splitlines()
#syntax=["import","echo"]

def write_syntax():
    with open('./storage/syntax.txt', 'w') as filehandle:
          json.dump(syntax, filehandle)
def read_syntax():
    with open('./storage/syntax.txt', 'r') as filehandle:
        global syntax
        syntax = json.load(filehandle)
read_syntax()
def call_func():
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
            val=input("q,x,r (use space as separator) || Enter lang type (w,c) and values of counter to save: ")
            m=1
            if val[0]=="x":
                filter=val[2:]
                splits=filter.split()
                for element in splits:
                    syntax.append(element)
                write_syntax()
                os.system('cls' if os.name == 'nt' else 'clear')
                call_func()
            elif val[0]=="q":
                with open('./storage/lang_dump_database.txt','w') as filehandle:
                    json.dump(data, filehandle)
                with open('./storage/last_lang.txt','w') as f:
                    f.write(str(lang))
                sys.exit()
            elif val[0]=="r":
                with open('./storage/review_later.txt','a+') as filehandle:
                    filehandle.write(str(lang)+"\n")
                    os.system('cls' if os.name == 'nt' else 'clear')
            else:
                type=val[0]
                local["type"]=type
                values_entered=val[2:]
                for i in values_entered.split():
                    local["code"+str(m)]=z[int(i)-1]
                    m=m+1
                    data[str(lang)]=local
                    os.system('cls' if os.name == 'nt' else 'clear')
with open('./storage/last_lang.txt','r') as f:
    last_lang=f.read().rstrip()
if last_lang=="":
    last_lang="!!!"
with open('./storage/lang_dump_database.txt','r') as filehandle:
    data = json.load(filehandle)
for lang in lines[lines.index(last_lang):]:
    call_func()
pprint.pprint(data)
with open('./storage/lang_dump_database.txt','w') as filehandle:
    json.dump(data, filehandle)
#implement storage in a file using dictionary
