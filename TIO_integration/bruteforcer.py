import json
from Tio import Tio
from multiprocessing.pool import ThreadPool as Pool

pool_size = 10

site=Tio()
flag_format=input("Enter the initials of the flag format: ")
input=input("Enter the esolang code: ")

global store
with open('./data/tio_lang_dump_database.txt','r') as filehandle:
    langs = json.load(filehandle)
xcept=0
def worker(lang):
    try:
        request=site.new_request(lang,input)
        output=site.send(request)
        if flag_format in output:
            print("Esolang found!! ",lang)
    except:
        xcept+=1
pool = Pool(pool_size)
for lang in langs:
    pool.apply_async(worker, (lang,))

pool.close()
pool.join()
