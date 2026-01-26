fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be Opened", fname)
    quit()
    
words = []
for line in fh:
    line = line.rstrip()
    line_words = line.split()

    for word in line_words:
        if word not in words:
            words.append(word)

words.sort()
print(words)






