fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    striped = line.rstrip()
    splited = striped.split()
    for word in splited:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
