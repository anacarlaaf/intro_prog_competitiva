n = int(input())
while len(str(n)) > 1:
    print(n)
    a = str(n)
    n = int(a[-1])+3*int(a[:-1])
print(n)
