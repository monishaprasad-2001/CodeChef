t = int(input())
for _ in range(t):
    a=list(map(int,input().split(" ")))
    o = a[0]
    s = a[1]
    if(o<s):
        print("BIKE")
    elif o>s:
        print("CAR")
    else:
        print("SAME")
