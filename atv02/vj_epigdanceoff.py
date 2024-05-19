import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
grid = []
for i in range(n):
    ln = input()
    ln = [a for a in ln]
    grid.append(ln)
points = 0
for i in range(m):
    empty = 0
    for j in range(n):
        if grid[j][i] == "$":
            break
        else:
            empty += 1
            if empty == n:
                points += 1
print(points+1)
