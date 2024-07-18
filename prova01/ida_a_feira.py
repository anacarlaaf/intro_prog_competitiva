# Problema: https://judge.beecrowd.com/pt/problems/view/1281

n = int(input())
for i in range(n):
    prods = {}
    qtd_produtos = int(input())
    for j in range(qtd_produtos):
        nome, price = input().split()
        price = float(price)
        prods[nome] = price
    qtd_comprar = int(input())
    total = 0
    for i in range(qtd_comprar):
        produto, qtd = input().split()
        qtd = int(qtd)
        total += prods[produto] * qtd
    txt = "R$ {pr:.2f}"
    print(txt.format(pr=total))
