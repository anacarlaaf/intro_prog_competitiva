n, q = map(int, input().split())
forest = []
for i in range(n):
    forest.append(list(input()))

# gerar matriz pra armazenar somas
# tamanho: n+1 x n+1, pra não dar erro nos indexes
pf_sum = []
for i in range(n+1):
    pf_sum.append([0 for k in range(n+1)])

# preencher matriz de prefix sum com ocorrências
for i in range(n):
    for j in range(n):
        if forest[i][j] == "*":
            pf_sum[i+1][j+1] = 1

# acumlar
for i in range(1, n+1):
    for j in range(1, n+1):
        pf_sum[i][j] += pf_sum[i-1][j] + pf_sum[i][j-1] - pf_sum[i-1][j-1]

# buscar
for i in range(q):
    y1, x1, y2, x2 = map(int, input().split())
    ans = pf_sum[y2][x2] - pf_sum[y1-1][x2] - pf_sum[y2][x1-1] + pf_sum[y1-1][x1-1]
    print(ans)
