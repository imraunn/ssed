import json
from collections import Counter

def charset_gen(input):
    storage=Counter(input)
    charsetlist=[]
    for element in storage:
        if element not in [" ","\n"]:
            charsetlist.append(element)
    return charsetlist
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

inp=input("Enter the type of esolang (w/c) followed by the code: ")
print()
type=inp[0]
code=inp[2:]

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
    for row in sort_frac_values:
        leng=len(lang)
        val=50-leng
        print("{:<50} {:<50}".format(round(row[1]*100),row[0]))
    print()
elif type=="w":
    print("word type in progress")
