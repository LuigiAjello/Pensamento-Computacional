lista = []
for i in range(9):
    numero = int(input("Digite um número: "))
    lista.append(numero)
primos = []
for numero in lista:
    if numero > 1:
        is_primo = True
        for i in range(2, numero):
            if numero % i == 0:
                is_primo = False
                break
        if is_primo:
            primos.append(numero)
print("Números primos na lista:", primos)
