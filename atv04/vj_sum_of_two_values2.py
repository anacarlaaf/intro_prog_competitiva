# Problema: https://vjudge.net/contest/630643#problem/C

n, x = map(int, input().split())
ar = list(map(int, input().split()))

# criar dict com os índices
indx = {}
for i in range(n):
    indx[ar[i]] = i+1

imp = True
for i in range(n):
    outro = x - ar[i]
    if outro in indx and indx[outro] != i + 1:  # verificar se chave existe em dict é O(1)
        print(i+1, indx[outro])
        imp = False
        break

if imp:
    print("IMPOSSIBLE")

# *quando encontrar um valor e o complemento for repetido, ele vai procurar
# no dict, porém o dict vai ter armazenado o último valor encontrado, logo
# os indexes vão ser diferentes: um do próprio i e outro armazenado no dict.
