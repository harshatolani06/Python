import re

line = 'From stephan.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#y = re.findall('@([^ ]*)',line)
#cooler regex version
y = re.findall('^From.*@([^ ]*)', line)
print(y)