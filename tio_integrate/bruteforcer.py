from Tio import Tio
site=Tio()
input=input()
request=site.new_request('python3',input)
print(site.send(request))
