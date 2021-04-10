import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
import os
import pprint
import sys
from freqanalysis import charset_gen,wordlist_gen

f=open("./langlist_scraper/database.txt","r",encoding="utf-8")
lines=f.read().splitlines()


def write_syntax():
    with open('./storage/syntax.txt', 'w',encoding="utf-8") as filehandle:
          json.dump(syntax, filehandle)
def read_syntax():
    with open('./storage/syntax.txt', 'r',encoding="utf-8") as filehandle:
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
            if all(word not in t for word in syntax):
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
            val=input("q,x,r,m (use space as separator) || Enter lang type (w,c) and values of counter to save: ")
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
                with open('./storage/lang_dump_database.txt','w',encoding="utf-8") as filehandle:
                    json.dump(data, filehandle)
                with open('./storage/last_lang.txt','w',encoding="utf-8") as f:
                    f.write(str(lang))
                sys.exit()
            elif val[0]=="r":
                with open('./storage/review_later.txt','a+',encoding="utf-8") as filehandle:
                    filehandle.write(str(lang)+"\n")
                    os.system('cls' if os.name == 'nt' else 'clear')
            elif val[0]=="m":
                type=val[1]
                if type == "c":
                    local["type"]="c"
                    values_entered=val[3:]
                    char_list=[]
                    for element in values_entered:
                        if element not in char_list:
                            char_list.append(element)
                    local["charset"]=char_list
                elif type == "w":
                    local["type"]="w"
                    words_entered=val[3:]
                    list_tmp=words_entered.split()
                    local["wordset"]=list_tmp
                data[str(lang)]=local
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                type=val[0]
                local["type"]=type
                values_entered=val[2:]
                storage_charset=set()
                storage_wordset=set()
                for i in values_entered.split():
                    if type == "c":
                        tmp_charset=set(charset_gen(z[int(i)-1]))
                        storage_charset=storage_charset.union(set(tmp_charset))
                        local["code"+str(m)]=z[int(i)-1][100:]
                    if type == "w":
                        local["code"+str(m)]=z[int(i)-1]
                        storage_wordset=storage_wordset.union(set(wordlist_gen(z[int(i)-1])))
                    m=m+1
                data[str(lang)]=local
                if type == "c":
                    local["charset"]=list(storage_charset)
                if type == "w":
                    local["wordset"]=list(storage_wordset)
                os.system('cls' if os.name == 'nt' else 'clear')
with open('./storage/last_lang.txt','r',encoding="utf-8") as f:
    last_lang=f.read().rstrip()
with open('./langlist_scraper/database.txt','r',encoding="utf-8") as f:
    firstline=f.readline().strip()
if last_lang=="":
    last_lang=firstline
with open('./storage/lang_dump_database.txt','r',encoding="utf-8") as filehandle:
    data = json.load(filehandle)
for lang in lines[lines.index(last_lang):]:
    call_func()
pprint.pprint(data)
with open('./storage/lang_dump_database.txt','w',encoding="utf-8") as filehandle:
    json.dump(data, filehandle)
