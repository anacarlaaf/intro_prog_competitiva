n = list(input())
letras = set(n)
tam = len(n)

palin = [" " for i in range(len(n))]
contar = {}  # um dict pra guardar quantas vezes os chars aparecem

for i in letras:
    contar[i] = n.count(i)

qtd_impares = 0
impar = ""
impar_index = 0
for i in contar:
    if contar[i] % 2 != 0:
        qtd_impares += 1
        impar = i
if qtd_impares == 1:
    n2 = sorted(n.copy())
    n2.remove(impar)
    for i in range(int(tam / 2)):
        palin[i] = n2[0]
        palin[-i - 1] = n2[1]
        del n2[:2]
    palin[int(tam/2)] = impar
    print("".join(palin))

elif qtd_impares == 0:
    n2 = sorted(n.copy())
    for i in range(int(tam/2)):
        palin[i] = n2[0]
        palin[-i-1] = n2[1]
        del n2[:2]
    print("".join(palin))
else:
    print("NO SOLUTION")
