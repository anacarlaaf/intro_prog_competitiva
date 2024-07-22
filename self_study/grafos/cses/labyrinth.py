from collections import deque

n, m = map(int, input().split())

inicio = ()
fim = ()
lab = []
for i in range(n):
    wall = input()
    for j in range(m):
        if wall[j] == "A":
            inicio = (i,j)
        elif wall[j] == "B":
            fim = (i,j)
    lab.append(wall)

pais = [[None]*m for _ in range(n)]
direcs = [[None]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
arrows = ["U", "D", "L", "R"]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_ok (k,l):
    if 0<=k<n and 0<=l<m:
        if not visited[k][l] and lab[k][l] != "#":
            return True
    else:
        return False

#bfs
q = deque([inicio])
visited[inicio[0]][inicio[1]] = True
possible = False

while q:
    a,b = q.popleft()
    if (a,b) == fim:
        possible = True
        break
    for k in range(4):
        x,y = a+dx[k], b+dy[k]
        if is_ok(x,y):
            q.append((x,y))
            visited[x][y] = True
            pais[x][y] = (a,b)
            direcs[x][y] = arrows[k]

tam = 0
if possible:
    path = [direcs[fim[0]][fim[1]]]
    print("YES")
    x, y = fim
    while True:
        tam += 1
        a,b = pais[x][y]
        if pais[x][y] == inicio:
            break
        else:
            path.append(direcs[a][b])
            x, y = pais[x][y]
    print(tam)
    path.reverse()
    print("".join(path))
else:
    print("NO")
