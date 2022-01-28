n = int(input())

for _ in range(n):
    arr=list(map(int,input().split(" ")))
    a = arr[0]
    b = arr[1]
    c = arr[2]
    print(sorted(arr)[1])
