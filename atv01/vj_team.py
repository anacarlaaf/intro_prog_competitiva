# Problema: https://codeforces.com/problemset/problem/231/A

n = int(input())
implement = 0
for i in range(n):
    a, b, c = map(int, input().split())
    if sum([a, b, c]) >= 2:
        implement += 1
print(implement)