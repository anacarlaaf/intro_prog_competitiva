n = int(input())
tasks = []
for i in range(n):
    a, d = map(int, input().split())
    tasks.append([a, d])

tasks.sort(key=lambda x: x[0])
time = 0
re = 0
for i in range(n):
    time += tasks[i][0]
    re += tasks[i][1] - time
print(re)