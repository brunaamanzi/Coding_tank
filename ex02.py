"""2. Você precisa implementar um código em Python que solicite ao usuário o valor principal (capital) inicial, a taxa de juros por período e o tempo em que o dinheiro é emprestado ou investido. Com base nesses valores, o programa deve calcular os juros simples e o montante total ao final do período. Assuma que temos apenas um único mês de investimento/empréstimo. Assinale a alternativa que corretamente implementa este procedimento:

a) juros = principal *= taxa
montante = principal + juros

b) juros = principal * taxa
montante = principal += juros

c) juros = principal *= taxa
montante = principal += juros

d) juros = principal + taxa
montante == principal ** juros

e) juros = principal * taxa
montante = principal + juros

Dica: O montante é calculado somando o principal ao juros e os juros são o produto do principal pela taxa."""
capital_inicial = float(input('Insira o Capital Inicial: R$'))
taxa_juros = float(input('Insira a taxa de juros no formato 0.0 a 1.0, sendo 0,0 = 0% e 1,0 = 100%: '))
tempo = int(input('Insira o número de meses em que o dinheiro ficará aplicado: '))
juros_simples = taxa_juros * capital_inicial
montante = capital_inicial+(capital_inicial*taxa_juros*tempo)
print(f'O valor referente aos juros simples a cada mês é de: R${juros_simples}')
print(f'O montante final é de R${montante}')
# A resposta correta é a letra e, visto que o juros é o capital inicial * taxa, e o montante é o capital inicial + (capital inicial * taxa), que pode ser substituído por capital inicial + juros.