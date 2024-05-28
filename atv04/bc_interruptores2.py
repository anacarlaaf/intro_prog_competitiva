# Problema: https://judge.beecrowd.com/pt/problems/view/2884

import sys
sys.stdin = open("input.txt", "r")

qtd_inter, qtd_lamp = map(int, input().split())

a = list(map(int, input().split()))
qtd_lamp_acessas = a[0]
lamp_acesas = a[1:]

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
    inter_lamps[i] = lamp
print(inter_lamps)

yes_no = {1: True, 0: False}
hist_status = []
clicks = 0
stop = False
soma = sum(lamp_stat.values())
while True:
    for i in range(1, qtd_inter+1):
        if soma == 0:
            stop = True
            print(clicks)
            break
        else:
            print(inter_lamps)
            print(lamp_stat)
            for j in inter_lamps[i]:
                if lamp_stat[j] == 1:
                    lamp_stat[j] = 0
                    soma -= 1
                else:
                    lamp_stat[j] = 1
                    soma += 1
                hist = list(lamp_stat.values())
                print(hist)
                if hist in hist_status:
                    print(-1)
                    stop = True
                    break
                else:
                    hist_status.append(hist)
                clicks += 1
            if stop:
                break
    if stop:
        break
