# cook your dish here
n = int(input())

for _ in range(n):
    arr=list(map(int,input().split(" ")))
    a = arr[0]
    b = arr[1]
    if a%b==0:
        print(a//b)
    else:
        print(-1)
