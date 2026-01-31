#without functions and get funtion
#counts = dict()
#names = ['csev','cwen','csev','zqian','cwen']
#for name in names:
#    if name not in counts:
#       counts[name] = 1
#    else:
#        counts[name]= counts[name]+1
#print(counts)


#with functions and get funtion
counts = dict()
print("Enter a line of text ")
line = input('')
words = line.split()
for word in words:
    counts[word] = counts.get(word,0) + 1
print('counts', counts)