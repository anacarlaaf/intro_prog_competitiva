# criar uma func pra gerar uma busca
# binária entre 1 e o maior tempo possiível

# criar uma func pra testar se esse tempo é ideal

n, t = map(int, input().split())
tempos = list(map(int, input().split()))
tempos.sort()

def total_time(time):
    total = 0
    for i in range(n):
        total += tempos[i]*time
    return total

def bs(ini, fim, find):
    meio = (ini+fim)//2
    best = 2*64
    if total_time(meio) < find:
        return bs(meio + 1, fim, find)
    else:
        if total_time(meio) == find:
            best = meio
            return bs(ini, meio-1, find)
    return best


print(bs(0,n-1,t))