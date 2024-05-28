# Problema: https://vjudge.net/contest/630643#problem/B

import sys
sys.stdin = open("input.txt", "r")

n, p, m = map(int, input().split())

ptc = {}
for i in range(n):
    name = input()
    ptc[name] = 0

winners = []
qtd_winners = 0
for i in range(m):
    name, pts = input().split()
    pts = int(pts)
    ptc[name] += pts
    if ptc[name] >= p and name not in winners:
        qtd_winners += 1
        print(name, "wins!")
        winners.append(name)

if qtd_winners == 0:
    print("No winner!")
