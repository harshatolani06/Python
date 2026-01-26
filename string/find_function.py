txt = "X-DSPAM-Confidence: 0.8475"
pos = txt.find(':')
value = txt[pos+2:]
fnum = float(value)
print(pos)
print(value)
print(fnum)