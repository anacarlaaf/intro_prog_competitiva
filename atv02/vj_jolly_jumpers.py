import sys
sys.stdin = open("input.txt", "r")

while True:
    try:
        tudo = input().split(" ")
        tudo = [int(i) for i in tudo]
        n = tudo[0]
        a = [i for i in tudo[1:]]
        pt = {True: "Jolly", False: "Not jolly"}

        jolly = True
        anterior = abs(a[0] - a[1]) + 1
        for i in range(1, len(a) - 1):
            dif = abs(a[i] - a[i - 1])
            if dif == anterior - 1:
                anterior = dif
            else:
                jolly = False
                break
        print(pt[jolly])
    except EOFError:
        break
