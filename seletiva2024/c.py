n = int(input())
apps = input()
tipos = set(apps)
qtd_tipos = len(tipos)

pegos = {}
for i in tipos:
    pegos[i] = 0

visitas = n
aux_pegos = {}
for i in range(n):
    aux_visitas = 0
    aux_pegos = pegos.copy()
    pokemons = 0
    for j in range(i, n):
        if aux_pegos[apps[j]] == 0:
            pokemons += 1
            aux_pegos[apps[j]] += 1
        aux_visitas += 1
        if pokemons == qtd_tipos:
            break
    if pokemons == qtd_tipos and aux_visitas < visitas:
        visitas = aux_visitas
print(visitas)
