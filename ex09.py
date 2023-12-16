"""9. Um grande banco deseja saber quais são seus produtos mais vendidos. Em uma lista, são registrados os nomes dos produtos, na ordem em que eles são vendidos (portanto, há elementos repetidos nesta lista). Faça um programa que exibe na tela cada um dos produtos na lista de input, e a quantidade em que eles foram vendidos (separados por um traço), de modo que teremos uma mensagem em cada linha. Os produtos devem ser exibidos em ordem alfabética.

Ex.: para a lista produtos = ["Crediário", "Consórcio", "Consórcio", "Financiamento", "Consórcio", "Crediário"]
Obs: Existem outros produtos além dos da lista acima, seu código deve contemplar outras possibilidades.
Devemos ter as seguintes mensagens exibidas na tela:
Consórcio - 3
Crediário - 2
Financiamento - 1"""

produtos = ["Crediário", "Consórcio", "Consórcio", "Financiamento", "Consórcio", "Crediário","Empréstimo"]
lista_ordenada = sorted(produtos)
for produto in set(lista_ordenada):
    print(f'{produto} - {produtos.count(produto)}')

