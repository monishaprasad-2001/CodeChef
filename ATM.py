ar = list(map(float,input().split(" ")))
num1 = ar[0]
num2 = ar[1]
if(num1>num2):
    print('%.2f' %num2)
else:
    if(num1%5==0):
        number =(num2-num1-0.50)
        print('%.2f' %number)
    else:
        print('%.2f' %num2)
