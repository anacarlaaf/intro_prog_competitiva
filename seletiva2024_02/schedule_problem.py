t = int(input())
for i in range(t):
    n = int(input())
    slot = {}
    flag = False
    for j in range(n):
        l, r = map(int, input().split())
        for k in range(l, r+1):
            slot[k] = slot.get(k, 0) + 1
            if slot[k] == n:
                flag = True
                break
    if flag:
        print("YES")
    else:
        print("NO")
