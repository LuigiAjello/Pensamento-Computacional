matriz_notas = []
for i in range(10):
    notas_aluno = []
    for j in range(3):
        nota = float(input(f"Nota {j + 1}: "))
        notas_aluno.append(nota)
    matriz_notas.append(notas_aluno)
menor_notas = [min(notas) for notas in matriz_notas]
provas_menor_nota = [notas.index(min(notas)) + 1 for notas in matriz_notas]
for i, prova in enumerate(provas_menor_nota, start=1):
    print(f"Aluno {i} teve a menor nota na prova {prova}")
contagem_prova1 = provas_menor_nota.count(1)
contagem_prova2 = provas_menor_nota.count(2)
contagem_prova3 = provas_menor_nota.count(3)
print("\nNúmero de alunos com menor nota em cada prova:")
print(f"Prova 1: {contagem_prova1}")
print(f"Prova 2: {contagem_prova2}")
print(f"Prova 3: {contagem_prova3}")
