# Problema: https://codeforces.com/problemset/problem/546/A

cost, dollars, bananas = map(int, input().split())

total = 0
for i in range(1, bananas+1):
    total += cost*i

if dollars >= total:
    print(0)
else:
    print(total-dollars)