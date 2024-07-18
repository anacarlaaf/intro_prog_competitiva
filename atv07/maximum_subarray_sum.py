n = int(input())
a = list(map(int, input().split()))

# kadane
maxx = -10**10
soma = -10**10
for i in range(n):
    if a[i] > a[i]+soma:
        soma = a[i]
    else:
        soma += a[i]
    if soma > maxx:
        maxx = soma
print(maxx)
