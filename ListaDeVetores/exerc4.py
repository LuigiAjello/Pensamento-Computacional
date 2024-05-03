modelos_carros = []
consumo_carros = []

print("Digite os modelos de cinco carros e seus consumos:")
for _ in range(5):
    modelo = input("Digite o modelo do carro: ")
    consumo = float(input("Digite o consumo do carro (em km/l): "))
    modelos_carros.append(modelo)
    consumo_carros.append(consumo)

indice_mais_economico = consumo_carros.index(min(consumo_carros))
modelo_mais_economico = modelos_carros[indice_mais_economico]

print(f"O modelo mais econômico é: {modelo_mais_economico}")

print("\nQuantidade de litros para percorrer 1000 km:")
for i in range(5):
    litros = 1000 / consumo_carros[i]
    print(f"{modelos_carros[i]}: {litros:.2f} litros")
