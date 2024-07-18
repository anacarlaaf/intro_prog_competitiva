import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    orders = list(map(int, sys.stdin.readline().split()))
    orders.sort()
    happy = 0
    total_candies = 0
    now_candies = 0
    for j in range(n):
        if orders[j] > now_candies:
            happy += 1
            total_candies += orders[j]
            now_candies += orders[j]
            # foi replicado não, só mudei a identação ._.
    print(happy, total_candies)
