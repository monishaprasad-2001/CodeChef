t = int(input())
def factorial(a):
    if a==0 or a==1:
        return(1)
    else:
        return (a*factorial(a-1))

a=[]

for _ in range(t):
    a.append(int(input()))

for x in a:
    print(factorial(x))
