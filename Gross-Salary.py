# cook your dish here
n = int(input())

for _ in range(n):
    basic = float(input())
    if basic<1500:
        print("{:.2f}".format(float(basic+(90/100)*basic+(10/100)*basic)))
    else:
        print("{:.2f}".format(float(basic+500+(98/100)*basic)))
