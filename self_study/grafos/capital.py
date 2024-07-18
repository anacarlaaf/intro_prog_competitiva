a,b,c,d = map(int, input().split())
l = [a,b,c,d]

def has_div(x,y):
    flagg = False
    if x != 1 and y != 1:
        flagg = True
    while y != 0:
        x, y = y, x % y
    if flagg and x == 1:
        return False
    else:
        return True

flag = True
for i in range(4):
    count = 0
    for j in range(4):
        if i != j and has_div(l[i], l[j]):
            count+=1
    if count < 2:
        flag = False
        break
    else:
        flag = True

if flag:
    print("S")
else:
    print("N")
