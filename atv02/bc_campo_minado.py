# Problema: https://judge.beecrowd.com/pt/problems/view/2399

import sys
sys.stdin = open("input.txt", "r")

n = int(input())

resultado = [0 for a in range(n)]
for i in range(n):
    bomb = int(input())
    if bomb == 1:
        resultado[i] += 1
        if i == 0:
            resultado[i+1] += 1
        elif i == n-1:
            resultado[i-1] += 1
        else:
            resultado[i-1] += 1
            resultado[i+1] += 1
for i in resultado:
    print(i)
