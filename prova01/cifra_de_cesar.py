# Problema: https://judge.beecrowd.com/pt/problems/view/1253

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

t = int(input())
for i in range(t):
    s = list(input())
    var = int(input())

    ans = []
    tam = len(s)
    for j in range(tam):
        andar = (alpha.index(s[j]) - var) % 26
        ans.append(alpha[andar])
    print("".join(ans))
