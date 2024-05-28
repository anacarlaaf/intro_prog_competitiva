# Problema: https://judge.beecrowd.com/pt/problems/view/1975

import sys
sys.stdin = open("input.txt", "r")

while True:
    qtd_perolas, qtd_alunos, qtd_respostas = map(int, input().split())

    if 0 == qtd_perolas == qtd_alunos == qtd_respostas:
        break

    perolas = []
    for i in range(qtd_perolas):
        perolas.append(input())

    alunos_perolas = {}
    for i in range(qtd_alunos):
        aluno = input()
        respostas = []
        for j in range(qtd_respostas):
            resposta = input()
            if resposta in perolas:
                alunos_perolas[aluno] = alunos_perolas.get(aluno, 0) + 1
        if aluno not in alunos_perolas.keys():
            alunos_perolas[aluno] = 0
    maior_aluno = []
    maior_perola = 0
    for i in alunos_perolas.keys():
        if alunos_perolas[i] > maior_perola:
            maior_aluno = [i]
            maior_perola = alunos_perolas[i]
        elif alunos_perolas[i] == maior_perola:
            maior_aluno.append(i)
    print(", ".join(sorted(maior_aluno)))
