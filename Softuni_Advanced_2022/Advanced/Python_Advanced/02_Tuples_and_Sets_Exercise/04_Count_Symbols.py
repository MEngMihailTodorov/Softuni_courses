mydict = {}
string = input()

for word in string:
    if word not in mydict.keys():
        d = {word: 1}
        mydict.update(d)
    else:
        mydict[word] += 1

for i in sorted(mydict.keys()):
    print(f"{i}: {mydict[i]} time/s")