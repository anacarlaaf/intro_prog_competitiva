# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())

for i in range(t):
    assentos, amigos = map(int, input().split())
    lista = input()
    vagas = (amigos+1)*"0"
    if vagas in lista:
        print("yes")
    else:
        print("no")
    