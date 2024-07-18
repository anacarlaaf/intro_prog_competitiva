from collections import deque

n, m = map(int, input().split())
floor = [[0 for o in range(m+2)] for p in range(n+2)]

for i in range(1,n+1):
    k = list(input())
    for j in range(1,m+1):
        floor[i][j] = k[j-1]

visited = [[False for o in range(m+2)] for p in range(n+2)]

def bfs(x,y):
    q = deque([])
    q.append((x,y))
    visited[x][y] = True
    while q:
        p = q.popleft()
        for j in [(p[0]-1,p[1]), (p[0]+1,p[1]), (p[0],p[1]-1), (p[0],p[1]+1)]:
            if not visited[j[0]][j[1]] and floor[j[0]][j[1]] == ".":
                q.append((j[0],j[1]))
                visited[j[0]][j[1]] = True

qts = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if not visited[i][j] and floor[i][j] == ".":
            bfs(i,j)
            qts += 1
print(qts)
