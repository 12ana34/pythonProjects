# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0
ipos = None
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ipos = line.find(':')
    total = total + float(line[ipos+2:])
    count = count + 1
print("Average spam confidence:",total/count)
