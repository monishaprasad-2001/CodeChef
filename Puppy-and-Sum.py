t=int(input())
def sum(d,n):
    for i in range(d):
        n=n*(n+1)//2
    return n


for i in range(t):
    d,n=map(int,input().split())
    print(sum(d,n))
