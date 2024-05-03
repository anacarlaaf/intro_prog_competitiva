# Problema: https://vj.csgrandeur.cn/81c566ac0d4de16114be3b9eced37614?v=1714559737

vpoints, m_meters = map(int, input().split())

altitudes = input().split()
altitudes = [int(i) for i in altitudes]

max_vpoints = 1
for i in range(vpoints):
    aux_max_vpoints = 1
    adicionar = 0
    for j in range(i+1, vpoints):
        adicionar = altitudes[j] - altitudes[j-1]
        if adicionar <= m_meters:
            aux_max_vpoints += 1
        else:
            break

    if aux_max_vpoints > max_vpoints:
        max_vpoints = aux_max_vpoints

print(max_vpoints)
