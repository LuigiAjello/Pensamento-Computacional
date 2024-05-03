temperaturas = []
meses_extenso = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
                "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
for i in range(1, 13):
    temperatura = float(input(f"Digite a temperatura média do mês {i}: "))
    temperaturas.append(temperatura)
maior_temperatura = max(temperaturas)
mes_maior_temperatura = meses_extenso[temperaturas.index(maior_temperatura)]
menor_temperatura = min(temperaturas)
mes_menor_temperatura = meses_extenso[temperaturas.index(menor_temperatura)]
print(f"A maior temperatura ocorreu em {mes_maior_temperatura} com {maior_temperatura} graus.")
print(f"A menor temperatura ocorreu em {mes_menor_temperatura} com {menor_temperatura} graus.")
