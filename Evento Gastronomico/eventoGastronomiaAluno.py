# Fornecedores do evento
dict_fornecedor = {
    0: {'nome': 'Pastel Frito', 'vendas': 3000},
    1: {'nome': 'Massa da Mama', 'vendas': 5000},
    2: {'nome': 'Pizza do Tio', 'vendas': 10000},
    3: {'nome': 'Rodizio Mineiro', 'vendas': 3900},
    4: {'nome': 'Restaurante para Todos', 'vendas': 6000},
    5: {'nome': 'Bom Prato', 'vendas': 9000},
    6: {'nome': 'Yakisoba Delicia', 'vendas': 3000},
    7: {'nome': 'Doceria Feliz', 'vendas': 8000},
    8: {'nome': 'Bolo Gostoso', 'vendas': 8900},
    9: {'nome': 'Carne Assada', 'vendas': 7400},
    10: {'nome': 'Panqueca na Hora', 'vendas': 10743},
    11: {'nome': 'Quibe Bem Feito', 'vendas': 8733},
    12: {'nome': 'Coxinha da Tia', 'vendas': 2999},
    13: {'nome': 'Brigadeiro do Ceu', 'vendas': 4500},
    14: {'nome': 'Feijoada Preta', 'vendas': 9022},
    15: {'nome': 'Sushi Baiano', 'vendas': 8444},
    16: {'nome': 'Peixe Grelhado', 'vendas': 19000},
    17: {'nome': 'Porco no Rolete', 'vendas': 4000},
    18: {'nome': 'Lanche Seja Feliz', 'vendas': 8000}
    }
# Clientes que consumiram no evento
list_cliente = ['rafael','douglas','amanda','jorge','jeffri','carol','cristian',
 'leonardo','maria','luana','vanessa','jose','maria','bento','mariana','saulo',
 'glauco','ze','maria','sandra','joao','mauro','tulio','romario','bebeto',
 'aldair','jose roberto','izabela','parreira','glauber','kim','arthur','leticia',
 'mario','solange','marcio','ludmila','luigi','emanuel','adriana','alan','lucas',
 'vitor','vitoria','zeca','tafarel','marcao','zuleica','abraao','davi','pedro',
 'bola','miguel','camila','xandao','alexandre','lula','zelia','mateus','almir',
 'daniel','daniela','nelio','collor','fabio','fabiana','ramalho','ducan',
 'mike','lebron','senna','pablo','pamela','pipen','gonçalo','piki',
 'nubia','eiji','otavio','patricia','elen','icaro','yumi','rafael','wilson',
 'fabricio','wagner','heitor', 'sandro', 'glaucia', 'george', 'pierre',
 'fabio', 'wanderley', 'wesley', 'beatriz', 'ivete', 'luciano', 'ricardo',
 'thome', 'josue', 'mateus', 'evandro', 'hellen', 'valber', 'zuleika', 'edvaldo',
 'galvao', 'eduardo', 'silvia','galileu','morais', 'claudia','nilvia']
# Despesas do evento
locacao = 0.10 # 10% das vendas
limpeza = 700
seguranca = 800
outras_despesas = 500

# 1 - Calcular o total de vendas usando o for loop no dict
total_vendas = 0
for fornecedor in dict_fornecedor.values():  
    total_vendas += fornecedor['vendas']
print(f"Total de vendas: {total_vendas}")
# Os professores doaram 5000,00, cada professor doou 1000,00
# 2 - Criar um dicionario com o nome e valor

dict_DoacoesProf = {
    "Laerte": 1000,
    "Glauceni": 1000,
    "Kerla": 1000,
    "Victor Hugo":  1000,
    "Sergio":  1000,
}
# 3 - Criar uma lista com os nomes dos professores
prof = list(dict_DoacoesProf)
list_prof = [prof]
print(list_prof)
# 4 - Adicionar essa lista dos professores na lista de clientes
list_cliente += prof
print(list_cliente)
# 5 - Calcular quantos pessoas estiveram e a media de gasto por pessoa

QuantidadeClientes= len(list_cliente)
print(list_cliente)

media = (total_vendas+5000) /QuantidadeClientes
print(media)

# 6 - Encontrar quem foi o 10 consumidor e retire da lista

list_cliente.pop(9)
print(list_cliente)

# 7 - Encontre o nome "bola" inserido incorretamente na lista e retire da lista

list_cliente.pop(list_cliente.index('bola'))
print(list_cliente)
# 8 - Verificar se todos os organizadores estao na lista
list_organizadores = ["Luigi", "Emanuel", "Ludmila"]
for organizador in list_organizadores:
    if organizador not in list_cliente:
        organizadores_presentes = False
        break
if organizadores_presentes:
    print("Todos os organizadores estão na lista de clientes.")
else:
    print("Alguns organizadores estão faltando na lista de clientes.")

# 9 - Tira-los da lista
for organizador in list_organizadores:
    try:
        index_organizador = list_cliente.index(organizador)
        list_cliente.pop(index_organizador)
    except ValueError:
        pass

# 10 - fazer uma funçao que calcule o lucro liquido do evento
# entrada dos parametros sao as vendas e as despesas
# criar um pacote e gravar o modulo com essa funcao
# criar um programa principal com a funcao main
# importe o pacote com a funcao
# chame a funcao dentro da programa principal main
# execute a programa principal main


