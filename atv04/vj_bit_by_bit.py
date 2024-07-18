# Problema: https://vjudge.net/contest/630643#problem/A

# O erro deve tar no and ou or

import sys
sys.stdin = open("input.txt", "r")

eq = {"0": False, "1": True}
while True:
    n = int(input())
    if n == 0:
        break
    bits = list(32*"?")
    for i in range(n):
        a = list(input().split())
        op = a[0]
        pos = list(map(int, a[1:]))
        if op == "CLEAR":
            bits[31-pos[0]] = "0"
        elif op == "SET":
            bits[31-pos[0]] = "1"
        elif op == "OR":
            if bits[31 - pos[0]] != "?" and bits[31 - pos[1]] != "?":
                if eq[bits[31-pos[0]]] or eq[bits[31-pos[1]]]:
                    bits[31-pos[0]] = "1"
                else:
                    bits[31 - pos[0]] = "0"
            elif bits[31-pos[0]] == "1" or bits[31-pos[1]] == "1":  # se for 1 ? ou ? 1 sabemos que é T
                bits[31 - pos[0]] = "1"
            else:
                bits[31 - pos[0]] = "?"
        else:
            if bits[31-pos[0]] != "?" and bits[31-pos[1]] != "?":
                if eq[bits[31-pos[0]]] and eq[bits[31-pos[1]]]:
                    bits[31-pos[0]] = "1"
                else:
                    bits[31-pos[0]] = "0"
            elif bits[31-pos[0]] == "0" or bits[31-pos[1]] == "0":  # se for ? 0 ou ? 0 já sabemos que é F
                bits[31 - pos[0]] = "0"
            else:
                bits[31-pos[0]] = "?"
    print("".join(bits))
