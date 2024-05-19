# Link do problema: https://vjudge.net/contest/626565#problem/D

while True:
    try:
        tudo = input().split(" ")
        tudo = [int(i) for i in tudo]
        n = tudo[0]
        a = [i for i in tudo[1:]]  # tira o n que diz quantos números são
        ynjolly = {True: "Jolly", False: "Not jolly"}
        jollies = [i for i in range(1, n)]

        jolly = True
        usadas = []
        for i in range(n-1):
            dif = abs(a[i] - a[i+1])
            usadas.append(dif)

        usadas.sort()
        for i in range(n-1):
            if usadas[i] == jollies[i]:
                jolly = True
            else:
                jolly = False
                break

        print(ynjolly[jolly])
    except EOFError:
        break
