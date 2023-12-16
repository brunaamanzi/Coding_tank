"""3. Na variável clientes_ano temos uma lista de listas, em que cada elemento é uma lista de dois elementos, o primeiro é o nome do cliente cadastrado na plataforma, e o segundo é o ano em que o cadastro foi realizado. Você deseja criar uma nova lista de listas (chamade de clientes_relacionamento), em que cada elemento é uma lista de dois elementos, sendo o primeiro o nome do cliente (como é na lista original), e o segundo é o número de anos em que o cliente está cadastrado na plataforma (considere que o ano atual é 2023). Qual das alternativas a seguir completa corretamente o trecho de código iniciado abaixo, para construir corretamente a lista desejada?"""

clientes_ano = [['Cliente A', 2018], ['Cliente B', 2021]] # Este é apenas um exemplo da lista dos anos
clientes_relacionamento = []

for lista in clientes_ano:
    clientes_relacionamento.append([lista[0], 2023 - lista[1]])
print(clientes_relacionamento)

"""Ao revisar este código, qual das alternativas a seguir produz o mesmo resultado?
a) clientes_relacionamento.append([lista[0], lista[1] - 2023])
b) clientes_relacionamento.append([lista[1], 2023 - lista[0]])
c) clientes_relacionamento.append([lista[1], lista[0] - 2023])
d) clientes_relacionamento.append([lista, 2023 - lista])
e) clientes_relacionamento.append([lista[0], 2023 - lista[1]])"""
# A resposta correta é a letra E, onde utilizamos a estrutura de repetição for e vamos varrendo cada lista dentro de clientes_ano, utilizamos o metodo append para ir adicionando ao final da nova lista criada as informações desejadas. lista[0] retorna o primeiro elemento de cada lista, enquanto lista[1] retorna o segundo elemento. precisamos inserir o ano antes da informação da lista[1] para não termos resultado negativo.