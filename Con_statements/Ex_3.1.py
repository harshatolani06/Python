hrs = input("Enter Hours:")
rate = input("Enter Rate:")
Eh = float(hrs)
Er = float(rate)

if Eh > 40:
    reg = Eh * Er
    oth = (Eh - 40.0) * (Er * 0.5)
    xp = reg + oth
else:
    xp = Eh * Er
    
print("Pay: " , xp)
    
    
    
