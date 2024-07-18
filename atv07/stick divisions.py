x, n = map(int, input().split())
sizes = set(list(map(int, input().split())))
sizes.sort(reversed=True)
sizes_s = set(sizes)

cost = 0
ped_1 = x//2
ped_2 = x - x//2
while ____:
    if ped_1 in sizes_s or ped_2 in sizes_s:
        x =
    else:
        ped_2 -= 1
        ped_1 += 2

print(cost)
