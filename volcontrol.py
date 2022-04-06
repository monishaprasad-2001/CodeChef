t = int(input())
for _ in range(t):
    a=list(map(int,input().split(" ")))
    n = a[0]
    m = a[1]
    print(abs(n-m))
