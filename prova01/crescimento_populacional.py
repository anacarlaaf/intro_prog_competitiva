# Problema: https://judge.beecrowd.com/pt/problems/view/1160

t = int(input())

for i in range(t):
    pa, pb, ga, gb = input().split()
    pa = int(pa)
    pb = int(pb)
    ga = float(ga)
    gb = float(gb)

    anos = 0
    while True:
        if anos > 100:
            break
        if pa > pb:
            break
        pa += ga*pa//100
        pb += gb*pb//100
        anos += 1
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(anos, "anos.")