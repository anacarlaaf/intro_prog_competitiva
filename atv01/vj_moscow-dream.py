# Problema: https://vjudge.net/problem/Kattis-moscowdream

a, b, c, n = map(int, input().split())
if n < 3 or a+b+c < n:
    print("NO")
else:
    if a == 0 or b == 0 or c == 0:
        print("NO")
    else:
        print("YES")
