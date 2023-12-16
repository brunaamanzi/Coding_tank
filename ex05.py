"""5. Em um banco, existe um sistema de alerta na central de suporte que é ativado quando o número de chamados supera 500. Enquanto o volume de chamados permanecer acima desse limite, o sistema exibe uma mensagem indicando quantos chamados ainda precisam ser resolvidos para que o número volte a ficar adequado. Para implementar esta lógica, você começou criando o seguinte código:"""

num_chamados = 780
while (num_chamados > 500):
    print(f'ALERTA! HÁ UM TOTAL DE {num_chamados}')
    print('Você atendeu um chamado!')
    print(f"Faltam {num_chamados - 500} para o nível estar dentro do aceitável!")
    num_chamados -= 1
print("\nNão estamos mais em estado de alerta!")

"""Assinale a alternativa que implementa corretamente a lógica desejada, substituindo o comentário no código acima:
a) num_chamados += 1
b) num_chamados = 100 - num_chamados
c) num_chamados -= 1
d) num_chamados = 100 + num_chamados
e) num_chamados += 100"""
# A alternativa correta é a letra C, pois é a única opção onde vamos subtraindo um chamado a cada rodada da estrutura de repetição while. A cada vez que o while roda, ele subtrai 1 do número total de chamados que ultrapassam o limite de 500.