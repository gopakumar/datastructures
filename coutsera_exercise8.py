#fname = input("Enter file name: ")
fh = open("romeo.txt")
lst = list()
words = list()
for line in fh:
    #print(line.rstrip())
    for word in line.split():
        if(word not in words):
            words.append(word)
words.sort()
print(words)

