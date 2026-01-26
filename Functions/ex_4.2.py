def computepay(hours, rate) :
    print("In computepay" , hours, rate)
    if hours > 40:
        reg = hours * rate
        oth = (hours - 40.0) * (rate * 0.5)
        pay = reg + oth
    else:
        pay = hours * rate
    print("returning", pay)
    return pay
    
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
Eh = float(hrs)
Er = float(rate)

xp = computepay(Eh, Er)
print("Pay: " , xp)