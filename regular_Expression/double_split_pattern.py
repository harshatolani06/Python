data = 'From stephan.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])