T = int(input())
arr=[]
for _ in range(T):
    arr.append(int(input()))

for i in range(T):
    print(int(str(arr[i])[::-1]))
