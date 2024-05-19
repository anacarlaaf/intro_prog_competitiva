t = int(input())
for i in range(t):
    n = int(input())
    estantes = int(n/5)
    if n%5 > 0:
        estantes+=1
    print(estantes)
    