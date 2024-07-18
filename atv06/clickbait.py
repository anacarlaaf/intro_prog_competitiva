n, k = map(int, input().split())

# ordenar? pesquisar ordenação de matriz
# fazer mat pra saber quais formulas vou usar aqui
# ir verificar em quantos momentos o primeiro atinge k sozinho
# a cada outro subtrair do total
vis = 0
mom = 0
for i in range(n):
    a, b = map(int, input().split())