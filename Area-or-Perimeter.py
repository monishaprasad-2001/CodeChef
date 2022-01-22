n1 = int(input())
n2 = int(input())
area = n1*n2
peri = 2*(n1+n2)
if area>peri:
    print("Area")
    print(area)
elif area<peri:
    print("Peri")
    print(peri)
else:
    print("Eq")
    print(area)
