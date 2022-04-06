t = int(input())
for _ in range(t):
    a=list(map(int,input().split(" ")))
    n = a[0]
    m = a[1]
    k = a[2]
    if (m-k)<n:
        print("No")
    else:
        print("Yes")
