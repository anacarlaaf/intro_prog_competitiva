n, m = map(int,input().split())

adj = [[] for i in range(n)]
for i in range(m):
    x, y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

