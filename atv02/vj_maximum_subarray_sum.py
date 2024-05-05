n = int(input())
a = input()
a = [int(i) for i in a.split()]

j = a[0]
maior_soma = -(2 ** 31)
soma = -(2 ** 31)
for i in a:
    if soma + i > i:
        soma += i
    else:
        soma = i
    if soma > maior_soma:
        maior_soma = soma
print(maior_soma)