# Problema: https://judge.beecrowd.com/pt/problems/view/2884

import sys
sys.stdin = open("input.txt", "r")

qtd_inter, qtd_lamp = map(int, input().split())

a = list(map(int, input().split()))
qtd_lamp_acessas = a[0]
lamp_acesas = a[1:]

qtd_lamp_acessas = int(qtd_lamp_acessas)
lamp_acesas = [int(i) for i in lamp_acesas]

lamp_stat = {}
for i in range(1,qtd_lamp+1):
    if i in lamp_acesas:
        lamp_stat[i] = 1
    else:
        lamp_stat[i] = 0
print(lamp_stat)

inter_lamps = {}
for i in range(1, qtd_inter+1):
    b = list(map(int, input().split()))
    k = b[0]
    lamp = b[1:]
    inter_lamps[i] = {j: lamp_stat[j] for j in lamp}

print(inter_lamps)
for i in inter_lamps:
    print(i, inter_lamps[i])

clicks = 0
while True:
    if sum(lamp_stat) == 0:
        print(clicks)
        break
    for i in range(1, qtd_inter+1):
        inter_lamps[i]