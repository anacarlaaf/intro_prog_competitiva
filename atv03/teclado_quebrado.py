# Link do problema: https://judge.beecrowd.com/pt/problems/view/1451

# Usar outro tipo de estrutura de dados: deque???
while True:
    try:
        txt = list(input())
        txt.append("]")
        tam = len(txt)

        beiju = []
        aux_beiju = []
        anterior = ""
        i = 0
        while i < tam:
            print(beiju)
            print(aux_beiju)
            if txt[i] == "[":
                if anterior == "[":
                    aux_beiju.extend(beiju)
                    beiju = aux_beiju
                else:
                    beiju.extend(aux_beiju)
                aux_beiju = []
                anterior = "["
            elif txt[i] == "]":
                if anterior == "[":
                    aux_beiju.extend(beiju)
                    beiju = aux_beiju
                    aux_beiju = []
                anterior = "]"
            elif txt[i] != "[" and txt[i] != "]":
                aux_beiju.extend(txt[i])
            if i == tam - 1:
                if anterior == "[":
                    aux_beiju.extend(beiju)
                    beiju = aux_beiju
                else:
                    beiju.extend(aux_beiju)
            i += 1
        print("".join(beiju))
    except EOFError:
        break
