# Problema: https://judge.beecrowd.com/pt/problems/view/2091

while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    oco = {}
    for i in range(n):
        oco[a[i]] = oco.get(a[i], 0) + 1
    for i in range(n):
        if oco[a[i]] % 2 != 0:
            print(a[i])
            break