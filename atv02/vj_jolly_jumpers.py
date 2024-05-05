import sys
sys.stdin = open("input.txt", "r")

while True:
    try:
        tudo = input().split(" ")
        tudo = [int(i) for i in tudo]
        n = tudo[0]
        a = [i for i in tudo[1:]]  # tira o n que diz quantos números são
        ynjolly = {True: "Jolly", False: "Not jolly"}

        jolly = True
        if len(a) == 1:
            print(ynjolly[jolly])
        else:
            anterior = abs(a[0] - a[1])
            for i in range(2, len(a)):
                dif = abs(a[i] - a[i - 1])
                print(a[i], a[i - 1])
                print(dif)
                if dif == anterior - 1:
                    anterior = dif
                else:
                    jolly = False
                    break
            print(ynjolly[jolly])
    except EOFError:
        break
