# Problema: https://judge.beecrowd.com/pt/problems/view/2091

import sys
sys.stdin = open("input.txt", "r")

while True:
    n = int(input())
    if n == 0:
        break
    vec = list(map(int, input().split()))
    oco = {}
    for i in range(n):
        oco[vec[i]] = oco.get(vec[i], 0) + 1
    for i in oco.keys():
        if oco[i] % 2 != 0:
            print(i)
            break
