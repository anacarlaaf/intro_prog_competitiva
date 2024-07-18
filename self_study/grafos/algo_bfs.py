from collections import deque

n = 0
fships = []
visited = [False for i in range(n)]
def bfs(s):
    q = deque([])
    q.append(s)
    visited[s] = True
    while q:
        q.popleft()

        for j in fships[s]:
            if not visited[j]:
                q.append(j)
                visited[j] = True

for i in range(n):
    if not visited[i]:
        bfs(i)