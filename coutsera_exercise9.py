#fname = input("Enter file name: ")
fname = "mbox-short.txt"
if len(fname) < 1 : fname = "mbox-short.txt"
word = list()
fh = open(fname)
#data = fh.read()
#print(dir(fh))
count = 0
for ln in fh:
    ln.strip()
    if ln.startswith("From") and not ln.startswith("From:"):
        #print (ln)
        word = ln.split()
        print(word[1])
        count = count+1
#print(data)

print("There were", count, "lines in the file with From as the first word")

