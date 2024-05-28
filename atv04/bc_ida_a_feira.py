# Problema: https://judge.beecrowd.com/pt/problems/view/1281

import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for i in range(t):
    qtd_produtos = int(input())
    produto_preco = {}
    for j in range(qtd_produtos):
        produto, preco = input().split()
        preco = float(preco)
        produto_preco[produto] = preco
    p = int(input())
    total = 0
    for k in range(p):
        pro_pedido, qtd = input().split()
        qtd = int(qtd)
        total += produto_preco[pro_pedido]*qtd
    print("R$ {total:.2f}".format(total=total))

