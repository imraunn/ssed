import re
from bs4 import BeautifulSoup
import json
data=open("./data/website_source.txt","r").read()
soup=BeautifulSoup(data,'html.parser')
div=soup.find_all("div", title=True)
list=[]
for z in div:
    lang=z['data-id']
    list.append(lang)
print(list)
with open('./data/tio_lang_dump_database.txt', 'w') as filehandle:
    json.dump(list, filehandle)
