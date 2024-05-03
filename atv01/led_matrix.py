# Problema: https://codeforces.com/gym/105053/problem/L

r, c, k = map(int, input().split())

da = True
for i in range(r):
    l, d = input().split()
    if "*" in d:
        if "-" in l:
            da = False
            break
    else:
        da = True

if da == True:
    print("Y")
else:
    print("N")