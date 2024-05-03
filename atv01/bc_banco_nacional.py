gra, pro, geo = map(int, input().split())
tipo = input()

maximo = 0
if tipo == "A":
    maximo = gra + int(pro*(3/2) + geo*(5/2))
elif tipo == "B":
    gra += geo*(5/2)
    maximo = pro + int(gra*(2/3))
else:
    gra += pro*(3/2)
    maximo = geo + int(gra*(2/5))
print(int(maximo))
