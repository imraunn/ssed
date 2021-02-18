from collections import Counter
storage=Counter('The quick brown fox jumped right over the lazy dog')
charsetlist=[]
for element in storage:
    print(element,":",storage[element])
    charsetlist.append(element)
