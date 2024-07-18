n, m, k = map(int, input().split())
desired = list(map(int, input().split()))
sizes = list(map(int, input().split()))
desired.sort()
sizes.sort()

sats = 0
ava = m
aps = 0
clis = 0
while True:
    if ava <= 0 or clis >= n or aps >= m:
        break
    if sizes[aps] < desired[clis]-k:
        aps += 1
    elif sizes[aps] > desired[clis]+k:
        clis += 1
    elif desired[clis]-k <= sizes[aps] <= desired[clis]+k:
        sats += 1
        aps += 1
        clis += 1
        ava -= 1
print(sats)