# Problema: https://vjudge.net/contest/630643#problem/C

n, x = map(int, input().split())
ar = list(map(int, input().split()))

# criar dict com os índices
indx = {}
for i in range(n):
    outro = x - ar[i]
    if outro in indx:  # verificar se chave existe em dict é O(1)
        print(i+1, indx[outro])
        break
    indx[ar[i]] = i+1
else:
    print("IMPOSSIBLE")
