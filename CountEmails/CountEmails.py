fname = input("Enter file name: ")
fh = open(fname)
lst = list()
count = 0
for line in fh:
    striped = line.rstrip()
    if striped.startswith('From '):
            splited = striped.split()
            lst.append(splited[1])
            count = count + 1

for email in lst:
    print(email)
print("There were", count, "lines in the file with From as the first word.")