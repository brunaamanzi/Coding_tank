"""7. Em um banco, é importante que tenhamos um registro de todos os clientes, sejam correntistas ou não, para que seja possível, por exemplo, realizar a comunicação com eles enviando ofertas de produtos.

Para começar a prototipar esta funcionalidade, você deve criar um programa em Python que leia diversos números inteiros e insira todos em uma lista (esses números são os identificadores dos clientes). A cada solicitação de número, pergunte ao usuário se deseja inserir outro número: tendo como resposta 'S' para inserir mais um; ou 'N' caso queira terminar. É possível que o mesmo número seja digitado mais de uma vez (isso pode representar o mesmo cliente fazendo mais de um pedido). Após construir a lista, mostre:

a) todos os números digitados na ordem em que foram inseridos
b) todos os números digitados em ordem crescente
c) a média destes valores
d) apenas os números pares
e) apenas os números ímpares
f) apenas os números repetidos

Obs.: O usuário obrigatoriamente digitará as letras S e N, contudo não necessariamente de forma padronizada."""
lista_clientes = []
escolha = "S"
while True:
        clientes = int(input('Insira o identificador do cliente: '))
        lista_clientes.append(clientes)
        while True:
            escolha = input('Deseja continuar? [S/N] ').upper()
            if escolha == "N" or escolha == "S": # utilizamos para aceitar se a informação foi apenas S/N, e pedir novamente até ser S/N
                break
        if escolha == "N": # Se "N", encerramos
            print(f'Registro encerrado.')
            break
print(f'Segue a lista com os números digitados na ordem em que foram inseridos: {lista_clientes}')
lista_ordenada = sorted(lista_clientes)
print(f'Segue a lista com os números digitados em ordem crescente: {lista_ordenada}')
média_valores = sum(lista_clientes)/len(lista_clientes)
print(f'Segue a média dos valores informados: {média_valores}')
lista_pares = []
lista_ímpares = []
for num in lista_clientes:
    if num % 2 == 0:
        lista_pares.append(num) # se o resto da divisão por 2 for = 0, é par
    else:
        lista_ímpares.append(num) # se o resto da divisão for diferente de 0, é ímpar
print(f'Segue os números pares informados: {lista_pares}')
print(f'Segue os números ímpares informados: {lista_ímpares}')
lista_repetição = []
for num in lista_clientes:
    if lista_clientes.count(num) > 1 and num not in lista_repetição:
        lista_repetição.append(num)
print(f'Segue os números que se repetem na lista: {lista_repetição}')



