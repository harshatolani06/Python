largest = None
smallest = None
num = 0
while True:
    num = input('Enter Number :')
    if num == 'done':
        break
    try:  
        fval = float(num)
        if largest is None or fval > largest:
            largest = fval
            # print(fval,largest,num,smallest)
        if smallest is None or fval < smallest:
            smallest = fval
    except:
        print('Invalid Number')
print('Largest Number is ', largest)
print('Smallest Number is ', smallest)
    