n, x = map(int, input().split())
a = list(map(int, input().split()))

qtd = 0
soma = 0
ocos = {0: 1}
for i in range(n):
    soma += a[i]
    if (soma - x) in ocos:
        qtd += ocos[soma - x]
    ocos[soma] = ocos.get(soma, 0) + 1
print(qtd)
