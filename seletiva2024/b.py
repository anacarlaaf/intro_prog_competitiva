t = int(input())

for i in range(t):
    tam = int(input())
    arrays = input().split()
    arrays = [int(a) for a in arrays]
    trocas = 0
    impares = 0
    pares = 0
    for b in range(tam):
        if b%2==0:
            if arrays[b]%2 != 0:
                impares += 1
        else:
            if arrays[b]%2 == 0:
                pares += 1
    if pares != impares:
        trocas = -1
    elif pares == impares and pares != 0:
        trocas = pares
    print(trocas)