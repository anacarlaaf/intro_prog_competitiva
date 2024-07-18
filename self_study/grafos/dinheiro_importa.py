n, m = map(int, input().split())

# lista com as dívidas
debts = []
for i in range(n):
    debts.append(int(input()))

# colocar na lisa de adjacências
fships = [[] for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    fships[x].append(y)
    fships[y].append(x)

# usar dfs para encontrar os vértices e partir dalí
visited = [False for i in range(n)]
pai = [-1 for i in range(n)]
def dfs(s):
    q = []
    q.append(s)
    visited[s] = True
    while q:
        p = q.pop()
        for j in fships[p]:
            if not visited[j]:
                q.append(j)
                visited[j] = True
                pai[j] = p

for i in range(n):
    if not visited[i]:
        dfs(i)

for i in range(n):
    if debts[i] < 0:


print(fships)
print(pai)
print(debts)
