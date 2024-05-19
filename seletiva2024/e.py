n = int(input())
lista = input().split()
lista = [int(i) for i in lista]

#mmc
lista.sort()
tam = len(lista)
mmc = []
for i in range(0, tam-1, 2):
    a = lista[i]
    b = lista[i+1]
    mc = []
    for j in range(2, 10):
        if a % j == 0 and b % j == 0:
            mc.append(j)
            print(j)
    mmc = 1
    for k in mc:
        mmc *= k
    print("mmc")
    print(mmc)
        
