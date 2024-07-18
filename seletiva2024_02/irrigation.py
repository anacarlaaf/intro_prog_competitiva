import sys
sys.stdin = open("input.txt", "r")
import heapq  # fila de prioridade

n, m, q = map(int, input().split())
cities = list(map(int, input().split()))

c_ocos = {}
for i in range(m):
    c_ocos[i+1] = 0

for i in range(n):
    c_ocos[cities[i]] += 1

heap = []
for i in range(1, m+1):
    heap.append((c_ocos[i], i))
heapq.heapify(heap)

last_year = n
years = {}
for i in range(q):
    k = int(input())
    if k > last_year:
        for j in range(last_year+1, k + 1):
            min_ocos, cidade = heapq.heappop(heap)
            years[j] = cidade
            min_ocos += 1
            heapq.heappush(heap, (min_ocos, cidade))
        last_year = k
    print(years[k])
