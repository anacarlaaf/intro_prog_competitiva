# Problema: https://vjudge.net/contest/630643#problem/C

n, x = map(int, input().split())
ar = list(map(int, input().split()))

l = 0
r = 1
soma = 0
idxs = []
found = False
while soma != x and l <= 0 or r <= 0:
    soma = ar[l] + ar[r]


if found:
    print(idxs[l, r])
else:
    print("IMPOSSIBLE")
