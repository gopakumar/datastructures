#fname = input("Enter file name: ")
fname = "mbox-short.txt"
if len(fname) < 1 : fname = "mbox-short.txt"
word = list()
maxhour = dict()
fh = open(fname)
#data = fh.read()
#print(dir(fh))
maxcount = 0
for ln in fh:
    ln.strip()
    #print (ln)
    if ln.startswith("From") and not ln.startswith("From:"):
        words = ln.split()
        for word in words:
            if(':' in word):
                hour = word.split(':')
                h = hour[0]
                #print (h)
                maxhour[h] = maxhour.get(h,0)+1

#print(maxhour.items())
sortedlist = sorted([(k,v) for (k,v) in maxhour.items()])
print (sortedlist)
vals = list()
for (k,v) in sortedlist:
    print(k,v)
    vals.append(v)
print(set(vals))
