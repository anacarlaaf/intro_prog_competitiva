n = int(input())
l = input()
pares = {"[":"]", "{":"}", "(":")"}

flag = True
pilha = []
for i in range(n):
    if l[i] in "({[":
        pilha.append(l[i])
    elif l[i] in "]})":
        if not pilha or l[i] != pares[pilha[-1]]:
            print(l[i], i)
            flag = False
            break
        else:
            pilha.pop()
if flag:
    print("ok so far")

