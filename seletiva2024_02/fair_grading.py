t = int(input())

for i in range(t):
    n = int(input())
    in_grades = list(map(int, input().split()))
    ne_grades = list(map(int, input().split()))

    grades = []
    total = 0
    for j in range(n):
        grades.append([in_grades[j], ne_grades[j]])
        total += in_grades[j]
    grades.sort()
    total -= grades[-1][0]
    total -= grades[0][0]
    grades.pop()
    del grades[0]

    best = 0
    add = 0
    take = 0
    for j in range(n-2):
        if grades[j][1] - grades[j][0] >= best:
            best = grades[j][1] - grades[j][0]
            take = grades[j][0]
            add = grades[j][1]

    total -= take
    total += add
    print(total)
