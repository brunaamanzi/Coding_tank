"""8. Escreva um código em Python que recebe um número (que possa ter casas decimais) e a escala de temperatura em que este valor se encontra e para qual ele deseja converter (Celsius, Kelvin ou Fahrenheit). Tanto na escala em que se encontra quanto para a que deseja converter, utilize as letras iniciais como entrada: Celsius - 'C', Kelvin - 'K' ou Fahrenheit - 'F'.

Seu código deve solicitar ao usuário as informações necessárias para realizar a conversão de temperatura (temperatura, escala_original, escala_convertida), de acordo com o template abaixo."""

temperatura = float(input('Insira a temperatura desejada: '))# código para receber o valor numérico da temperatura desejada
while True:
    escala_original = input(
        "Em qual Escala de Temperatura esse valor se encontra? (C/K/F) ").upper()  # código para receber a escala original da temperatura informada
    if escala_original == "C" or escala_original == "K" or escala_original == "F":
        break
while True:
    escala_convertida = input("E para qual Escala de Temperatura você deseja converter? (C/K/F) ").upper() # código para receber a escala para a qual deseja-se converter a temperatura
    if escala_convertida == "C" or escala_original == "K" or escala_original == "F":
        break
if escala_original == "C":
    if escala_convertida == "C":
        print(f'A temperatura informada é de {temperatura}ºC')
    elif escala_convertida == "K":
        kelvin = temperatura + 273.15
        if kelvin < 0:
            print(f'Valor inválido.')
        else:
            print(f'A temperatura informada é de {kelvin}ºK')
    elif escala_convertida == "F":
        fahrenheit = (9/5 * temperatura) + 32
        print(f'A temperatura informada é de {fahrenheit}ºF')
if escala_original == "K":
    if escala_convertida == "C":
        celsius = temperatura - 273.15
        print(f'A temperatura informada é de {celsius}ºC')
    elif escala_convertida == "K":
        print(f'A temperatura informada é de {temperatura}ºK')
    elif escala_convertida == "F":
        fahrenheit = (temperatura - 273.15) * 9 / 5 + 32
        print(f'A temperatura informada é de {fahrenheit}ºF')
if escala_original == "F":
    if escala_convertida == "C":
        celsius = (temperatura - 32) * 5 / 9
        print(f'A temperatura informada é de {celsius}ºC')
    elif escala_convertida == "K":
        celsius = (temperatura - 32) * 5 / 9
        kelvin = celsius + 273.15
        print(f'A temperatura informada é de {kelvin}ºK')
    elif escala_convertida == "F":
        print(f'A temperatura informada é de {temperatura}ºF')






"""Implemente abaixo toda a lógica de conversão de temperaturas, bem como as validações necessárias.

Importante: o programa deve trabalhar apenas com as 3 escalas supracitadas! Então, não deixe de fazer as validações necessárias. Além disso, por definição, não existem temperaturas em Kelvin abaixo de zero (o valor zero pode existir), portanto verifique também esta condição para que sejam feitas conversões válidas!"""

