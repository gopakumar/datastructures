#fname = input("Enter file name: ")
fname = "mbox-short.txt"
if len(fname) < 1 : fname = "mbox-short.txt"
word = list()
maxemail = dict()
fh = open(fname)
#data = fh.read()
#print(dir(fh))
maxcount = 0
for ln in fh:
    ln.strip()
    if ln.startswith("From") and not ln.startswith("From:"):
        #print (ln)
        word = ln.split()
        #print(word[1])
        maxemail[word[1]] = maxemail.get(word[1],0)+1
        if maxcount < maxemail[word[1]] :
            maxcount = maxemail[word[1]]
            email = word[1]
#print(maxemail.items())
print (email,maxcount)
#print("There were", maxcount, "lines in the file with From as the first word")

