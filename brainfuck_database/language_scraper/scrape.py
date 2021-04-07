import requests
import re
from bs4 import BeautifulSoup
import urllib.parse

url="https://esolangs.org/wiki/Category:Brainfuck_equivalents"
page=requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
f=open("database.txt","w")
for link in soup.findAll('a', attrs={'href': re.compile("(?=.*^[^:]+$)(?=.*^/wiki/)")})[1:-3]:
    print(link)
    output=urllib.parse.unquote(link.get('href')[6:])
    f.write(output+'\n')
f.close()
