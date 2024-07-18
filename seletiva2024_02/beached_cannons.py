t = int(input())
for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())

    a = (y2*x1-x2*y1)/(x1*x2**2-x1**2*x2)
    b = (y1-a*x1**2)/x1
    x_ver = -b/(2*a)
    print("{x:.15f}".format(x=2*x_ver))