t = int(input())
for _ in range(t):
    a=list(map(int,input().split(" ")))
    c = a[0]
    x = a[1]
    y = a[2]
    print((c-x)*y)
