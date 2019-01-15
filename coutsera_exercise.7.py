# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fname = "mbox-short.txt"
fh = open(fname)
sum = 0.0
count =0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line)
    pos = line.find("0")
    #print(line[pos:])
    sum = sum+float(line[pos:])
    count = count+1
    avg= float(sum/count)
print (avg)
print("Done")
