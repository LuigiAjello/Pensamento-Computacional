x = []
y = []
ListaSoma = []
ListaSubtra = []
ListaProd = []

print("Digite 10 valores para x:")
for i in range(10):
    numero = int(input("Digite um número para x: "))
    x.append(numero)
    
print("Digite 10 valores para y:")
for i in range(10):
    numero = int(input("Digite um número para y: "))
    y.append(numero)

for i in range(10):
    soma = x[i] + y[i]
    subtra = x[i] - y[i]
    prod = x[i] * y[i]
    ListaSoma.append(soma)
    ListaSubtra.append(subtra)
    ListaProd.append(prod)

print("Lista de soma dos elementos correspondentes em x e y:", ListaSoma)
print("Lista de subtração dos elementos correspondentes em x e y:", ListaSubtra)
print("Lista de produto dos elementos correspondentes em x e y:", ListaProd)
