# Problema: https://judge.beecrowd.com/pt/problems/view/1424

while True:
    try:
        flag = False
        n, m = map(int, input().split())
        ve = list(map(int, input().split()))
        ocos = {}
        oco_index = {}
        for i in range(n):
            ocos[ve[i]] = ocos.get(ve[i], 0) + 1
            oco_index.setdefault(ve[i], []).append(i+1)
        for i in range(m):
            k, v = map(int, input().split())
            if v in oco_index and ocos[v] >= k:
                print(oco_index[v][k-1])
            else:
                print(0)
    except EOFError:
        break