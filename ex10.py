"""10. Um banco está analisando o desempenho de um investimento ao longo de um mês. Eles têm uma lista de valores de fechamento diários deste investimento e querem calcular uma média móvel de 7 dias para entender melhor as tendências no curto prazo. A média móvel de 7 dias é uma forma comum de suavizar flutuações diárias, dando ao banco uma visão mais clara das tendências de desempenho do investimento.

Seu objetivo é desenvolver um código em Python que processe a lista de valores fornecida. O código deve calcular e retornar uma nova lista contendo a média móvel de 7 dias para cada período possível dentro dos dados fornecidos.

Dica: A média móvel em um determinado dia é calculada como a média dos valores de fechamento dos 7 dias anteriores, incluindo o dia atual."""

valores_dos_fechamentos = [
    156.89, 155.16, 148.41, 145.18, 150.23, 148.10, 155.68,
    146.07, 149.53, 151.67, 158.16, 150.09, 145.64, 155.12,
    152.37, 145.01, 158.19, 159.66, 156.20, 158.04, 146.20,
    154.60, 157.98, 153.68, 149.44, 142.01, 148.68, 152.22,
    158.26, 159.33
]

for i in range(6, len(valores_dos_fechamentos)):
    media = sum(valores_dos_fechamentos[i-6:i+1]) / 7
    print(f"Média Móvel de 7 dias no dia {i+1}: {round(media, 2)}")

