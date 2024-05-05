n = list(input())
n = sorted(n)
tam = len(n)
palin = [" " for i in range(tam)]

controle = 0
no_solution = False
if tam % 2 == 0:
    for i in range(int(tam/2)):
        if n[controle] == n[controle+1]:
            palin[i] = n[controle]
            palin[-i-1] = n[controle+1]
            controle += 2
        else:
            no_solution = True
            break
    if no_solution:
        print("NO SOLUTION")
    else:
        print("".join(palin))

else:
    impares = 0
    tam2 = int(tam / 2)
    meio = " "
    for i in range(tam2):
        if n[controle] == n[controle + 1]:
            palin[i] = n[controle]
            palin[-i - 1] = n[controle + 1]
            controle += 2
        else:
            impares += 1
            if impares > 1:
                impares += 1
                break
            else:
                meio = n[controle]
                palin[i] = n[controle + 1]
                palin[-i - 1] = n[controle + 2]
                controle += 3
                palin[int(tam/2)] = meio
    if impares == 0:
        meio = n[-1]
        palin[int(tam / 2)] = meio
        print("".join(palin))
    elif impares == 1 and palin[0] == palin[-1]:
        palin[int(tam / 2)] = meio
        print("".join(palin))
    else:
        print("NO SOLUTION")
