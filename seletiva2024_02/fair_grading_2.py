t = int(input())
for i in range(t):
    n = int(input())
    in_grades = list(map(int, input().split()))
    ne_grades = list(map(int, input().split()))

    total = sum(in_grades)
    pares = []
    for j in range(n):
        pares.append([in_grades[j], ne_grades[j]])
    pares.sort()
    max = pares[-1][0]
    min = pares[0][0]

    take = 0
    put = 0
    best = 0
    for j in range(n):
        if pares[j][1] <= max and pares[j][1] - pares[j][0] > best:
            best = pares[j][1] - pares[j][0]
            take = pares[j][0]
            put = pares[j][1]
    print(total-take+put-(max+min))
