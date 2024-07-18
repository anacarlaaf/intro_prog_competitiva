n = int(input())
time = []
for i in range(n):
    a, b = map(int, input().split())
    time.append([a, b])

time.sort(key=lambda x: x[1])
mais_cedo = time[0][1]
total = 1
for i in range(n):
    if time[i][0] >= mais_cedo:
        total += 1
        mais_cedo = time[i][1]
print(total)
