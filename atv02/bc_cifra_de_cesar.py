# Problema: https://judge.beecrowd.com/pt/problems/view/1253

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
for i in range(n):
    cod = input()
    deslocamento = int(input())

    alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decod = ""
    descod = 0
    for j in cod:
        ind_alfa = alfa.index(j)
        descod = ind_alfa - deslocamento
        decod += alfa[descod]
    print(decod)
