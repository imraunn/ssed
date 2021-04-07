import json
import re
from collections import Counter
import argparse
import pyfiglet
import os

os.system('cls' if os.name == 'nt' else 'clear')
print(pyfiglet.figlet_format("S S E D"),end="")
print("\t\t -justanothern00b\n")

parser = argparse.ArgumentParser(
    description="Semi Smart Esolang Decrypter's CLI",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("path", type=str, help="File path to take input from")
parser.add_argument("type", type=str, help="w/c on the basis of which type of esolang")
args = parser.parse_args()
print()
file_path=args.path
file_type=args.type
content=open(file_path,'r')
file_input=content.read()

def charset_gen(input):
    storage=Counter(input)
    charsetlist=[]
    for element in storage:
        if element not in [" ","\n"]:
            charsetlist.append(element)
    return charsetlist
def wordlist_gen(input):
    return input.split()

def math_freq(charset_input,charset_database):
    a=len(charset_database)
    b=len(charset_input)
    counter1=0
    counter2=0
    for element in charset_input:
        if element in charset_database:
            counter1=counter1+1
        else:
            counter2=counter2+1
    z=counter1
    y=counter2
    fraction=((2*z)/(a+b))-0.2*((2*y)/(a+b))
    if y==0:
        fraction=fraction+0.8*(a-b)/(a+b)
    #print(z,y,a,b)
    return fraction

with open('./database.txt', 'r') as filehandle:
    global database
    database = json.load(filehandle)
print()
type=file_type
code=file_input

frac_values={}

if type=="c":
    charset_input=charset_gen(code)
    for lang in database.keys():
        if (database[lang])["type"] == "c":
            charset_database=(database[lang])["charset"]
            perc=math_freq(charset_input,charset_database)
            frac_values[lang]=perc
    sort_frac_values = sorted(frac_values.items(), key=lambda x: x[1], reverse=True)
    print("{:<50} {:<50}".format('Percentage','Language'))
    print()
    top=1
    for row in sort_frac_values:
        if top<=10:
            print("{:<50} {:<50}".format(round(row[1]*100),"https://esolangs.org/wiki/"+row[0]))
            top=top+1
        elif top==11:
            print()
            yon=input("Would you like to view the code of any of the above language? (y/n) ")
            if yon=="y":
                top=top+1
                ranking=input("Which language? Please enter the position in ranking: ")
                nameoflang=sort_frac_values[int(ranking)-1][0]
                print()
                print(nameoflang)
                print()
                local=database[nameoflang]
                for key in local.keys():
                    if "charset" in key:
                        print(local[key])
                        print()
            else:
                print()
                exit()
elif type=="w":
    wordset_input=wordlist_gen(code)
    for lang in database.keys():
        langval=0
        if (database[lang])["type"] == "w":
            wordset_database=(database[lang])["wordset"]
            for word in wordset_input:
                for compare in wordset_database:
                    regex_exp="(?i)^"+word+"$"
                    if bool(re.search(regex_exp,compare))==True and len(word)>=2:
                        langval=langval+1
            frac_values[lang]=langval
    sort_frac_values = sorted(frac_values.items(), key=lambda x: x[1], reverse=True)
    print("{:<50} {:<50}".format('Hits','Language'))
    print()
    top=1
    for row in sort_frac_values:
        if top<=10:
            print("{:<50} {:<50}".format(round(row[1]),"https://esolangs.org/wiki/"+row[0]))
            top=top+1
        elif top==11:
            print()
            yon=input("Would you like to view the codes of any of the above language? (y/n) ")
            if yon=="y":
                top=top+1
                ranking=input("Which language? Please enter the position in ranking: ")
                nameoflang=sort_frac_values[int(ranking)-1][0]
                print()
                print(nameoflang)
                print()
                local=database[nameoflang]
                for key in local.keys():
                    if "wordset" in key:
                        print(local[key])
                        print()
            else:
                print()
                exit()
