# Problema: https://judge.beecrowd.com/pt/problems/view/3464

import sys
sys.stdin = open("input.txt", "r")

# dimensoes do grid
n, m = map(int, input().split())
s = int(input())  # qtd de sensores

# gerar o grid com todos 0
grid = [[0 for i in range(m)] for j in range(n)]

n -= 1
m -= 1

# pegar a coordinated e o alcance dos sensores
for i in range(s):
    x, y, r = map(int, input().split())
    # verificar se a área coberta pelo sensor está inteira dentro do setor
    # coluna:
    # LEMBRAR QUE TUDO CONTA A PARTIR DE 1 NÃO 0
    x -= 1
    y -= 1

    # linha
    if y - r > 0:
        c_linha = y - r
    else:
        c_linha = 0
    if y + r < n:
        f_linha = y + r
    else:
        f_linha = n
    # coluna:
    if x - r > 0:
        c_coluna = x - r
    else:
        c_coluna = 0
    if x + r > m:
        f_coluna = x + r
    else:
        f_coluna = m

    # add 1 às posições começando da coluna e linha
    for ll in range(c_linha, f_linha):
        for c in range(c_coluna, f_coluna):
            print(ll, c)
            grid[ll][c] += 1
        for k in grid:
            print(k)

for i in grid:
    print(i)
