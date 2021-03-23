from Tio import Tio
site=Tio()
input=input()
request=site.new_request('cpp-gcc',input)
output=site.send(request)
flag="Exit code: "
if flag in output:
    split = output.index(flag)
    error_code = output[split+11:]
    print(error_code)
