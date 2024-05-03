primeiro_vetor = []
segundo_vetor = []

print("Preencha o primeiro vetor com 10 números inteiros:")
for _ in range(10):
    numero = int(input("Digite um número inteiro: "))
    primeiro_vetor.append(numero)

print("Preencha o segundo vetor com 5 números inteiros:")
for _ in range(5):
    numero = int(input("Digite um número inteiro: "))
    segundo_vetor.append(numero)

vetor_pares = []
vetor_impares = []

for num1 in primeiro_vetor:
    for num2 in segundo_vetor:
        soma = num1 + num2
        if soma % 2 == 0:
            vetor_pares.append(soma)
        else:
            vetor_impares.append(soma)

print("Vetor de números pares resultantes:", vetor_pares)
print("Vetor de números ímpares resultantes:", vetor_impares)
