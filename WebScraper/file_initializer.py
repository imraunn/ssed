import json
syntax=[]
data={}
with open('lang_dump_database.txt', 'w') as filehandle:
    json.dump(data, filehandle)
with open('syntax.txt', 'w') as filehandle:
      json.dump(syntax, filehandle)
open('last_lang.txt', 'w').close()
