name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
dic = dict()
handle = open(name)
for line in handle:
    striped = line.rstrip()
    words = striped.split()
    if len(words) < 5 or words[0] != 'From':
        continue
    time = words[5].split(':')
    dic[time[0]] = dic.get(time[0], 0) + 1

for k,v in sorted(dic.items()):
    print(k, v)

