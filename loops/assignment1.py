num = 0
sum = 0.0
while True:
    #print('before',sum, num)
    sval = input("Enter a Number : ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
    num = num + 1
    sum = sum + fval
print(sum,num,sum/num)
    

