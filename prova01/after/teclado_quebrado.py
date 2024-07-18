# Problema: https://judge.beecrowd.com/pt/problems/view/1451
# usar deque para não dar time nem memmory limit

from sys import stdin, stdout


def main():
    while True:
        try:
            l = stdin.readline()
            ans = []
            aux = []
            home = False
            for i in l:
                if i == "\n":
                    continue
                if i != "[" and i != "]" and not home:
                    ans.append(i)
                elif i != "[" and i != "]" and home:
                    aux.append(i)
                else:
                    if i == "[":
                        home = True
                    else:
                        home = False
                        aux.extend(ans)
                        ans = aux
            if home:
                aux.extend(ans)
                ans = aux
            stdout.write("".join(ans)+"\n")
        except EOFError:
            break


if __name__ == "__main__":
    main()
