import json
syntax=[]
data={}
with open('./storage/lang_dump_database.txt', 'w') as filehandle:
    json.dump(data, filehandle)
with open('./storage/syntax.txt', 'w') as filehandle:
      json.dump(syntax, filehandle)
open('./storage/last_lang.txt', 'w').close()
open('./storage/review_later.txt', 'w').close()
