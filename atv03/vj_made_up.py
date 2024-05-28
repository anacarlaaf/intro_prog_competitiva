n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

count_b = {}
for i in range(n):
    count_b[b[i]] = count_b.get(b[i], 0) + 1
print(count_b)

count_a = {}
for i in range(n):
    count_a[a[i]] = count_a.get(a[i], 0) + 1
print(count_a)

map_c = {}
for i in c:
    if i <n:
        k = b[i]
        map_c[b[i]] = map_c.get(k, 0) + 1
print(map_c)

pares = 0
for i in map_c.keys():
    pares += map_c[i]*count_a[i]*count_b[i]

print(pares)
