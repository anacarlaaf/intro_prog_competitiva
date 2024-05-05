def f(n, tamanho):
    if tamanho == 1:
        return n
    else:
        a = [int(i) for i in n]
        soma = 0
        if tamanho % 2 == 0:
            for i in range(tamanho//2):
                soma += a[i] + a[-i-1]
        else:
            for i in range((tamanho-1)//2):
                soma += a[i] + a[-i-2]
            soma += a[-1]
        tamanho2 = len(str(soma))
        lista = [int(i) for i in str(soma)]
        return f(lista, tamanho2)


while True:
    b = input()
    if b == "0":
        break
    else:
        tam = len(b)
        print(f(b, tam)[0])
