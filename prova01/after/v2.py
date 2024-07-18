while True:
    try:
        tex = list(input())
        ans = []
        tam = len(tex)
        i = 0
        aux1 = []
        aux2 = []
        home = False
        while True:
            if i == tam:
                if not home:
                    ans.extend(aux1)
                else:
                    aux1.extend(ans)
                    ans = aux1
                break
            if tex[i] != "[" and tex[i] != "]":
                aux1.append(tex[i])
            else:
                if tex[i] == "[":
                    home = True
                else:
                    home = False
                if home:
                    ans.extend(aux1)
                aux1 = []
            i += 1
        print("".join(ans))
    except EOFError:
        break