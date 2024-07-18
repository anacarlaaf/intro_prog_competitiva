import sys
sys.stdin = open("input.txt", "r")

def binary_search(item, arr, tam):
    best = -1
    best_len = 10**6
    inicio, final = 0, tam-1
    while inicio <= final:
        meio = (inicio+final)//2
        now_len = len(arr[meio])
        if item in arr[meio] and now_len <= best_len:
            best = meio
            best_len = now_len
            final = meio - 1
        elif arr[meio] > item:
            final = meio-1
        else:
            inicio = meio+1
    return best


n, q = map(int, input().split())
words = []
for i in range(n):
    words.append(input())
words.sort()

for i in range(q):
    find = input()
    idx = binary_search(find, words, n)
    if idx != -1:
        found = words[idx]
        print(len(found)-len(find))
    else:
        print(-1)