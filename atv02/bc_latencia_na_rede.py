# Problema: https://judge.beecrowd.com/pt/problems/view/3464

import sys
sys.stdin = open("input.txt", "r")

# dimensoes do grid
n, m = map(int, input().split())
s = int(input())  # qtd de sensores

for i in range(s):
    x, y, r = map(int, input().split())
