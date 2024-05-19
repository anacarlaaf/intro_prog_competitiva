n = int(input())
pesos = input().split()
pesos = [int(i) for i in pesos]
pesos.sort()

instab = 0
min_instab = max(pesos)
for i in range(2*n):
    for j in range(2*n):
        if i != j:
            instab = 0
            a = 0
            while True:
                if a == n/2:
                    break
                else:
                    if a != i and a != j:
                        instab += abs(pesos[a] - pesos[a + 1])
                        a += 2
                    else:
                        a += 1
            if instab < min_instab:
                min_instab = instab
print(instab)
