from collections import Counter
def charset_gen(input):
    storage=Counter(input)
    charsetlist=[]
    for element in storage:
        if element not in [\n"]:
            charsetlist.append(element)
    return charsetlist
def wordlist_gen(input):
    return input.split()
