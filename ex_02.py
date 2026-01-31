fname = input("Enter Your File Name ")
if len(fname) <1: fname = 'clown.txt'

fhand = open(fname)
many = dict()
for line in fhand:
	line = line.rstrip()
	wds = line.split()
	for w in wds:
		many[w] = many.get(w,0) + 1
#find the word with the largest count
largest = None
for cle, value in many.items():
	print(cle, value)
	if largest is None or largest <  value:
		largest = value
print('yay!!',largest)			
      


















