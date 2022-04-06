t = int(input())
for _ in range(t):
    a=list(map(int,input().split(" ")))
    n = a[0]
    m = a[1]
    if n<m:
        print(n)
    elif n==m:
        print(n)
    elif n>m:
        print((n-m)+n)
