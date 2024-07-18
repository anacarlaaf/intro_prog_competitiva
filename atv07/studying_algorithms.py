n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
soma = 0
qtd = 0
for i in range(n):
    if soma+a[i] > x:
        break
    soma += a[i]
    qtd += 1
print(qtd)