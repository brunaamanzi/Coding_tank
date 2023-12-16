"""6. Imagine que você está desenvolvendo um aplicativo para planejamento de viagens rodoviárias. Uma das funcionalidades desse aplicativo é ajudar os usuários a estimar o tempo que levarão para chegar a seus destinos. Para tornar o aplicativo mais interativo e educativo, você decide incluir uma seção onde os usuários podem calcular a distância de uma viagem baseando-se na velocidade média esperada do veículo e no tempo de viagem. Faça um código em Python que calcule a distância em km entre duas cidades, completando o template de código a seguir, no qual o tempo em minutos deve ser informado pelo usuário:"""

velocidade = 25 # esta em m/s
velocidade_convertida = velocidade * 3.6  # código para colocar a velocidade na unidade adequada
tempo = float(input('Insira o tempo em minutos estimado para sua viagem: '))     # código para receber como input do usuário o tempo em minutos
distancia = velocidade_convertida * (tempo/60) # código que implementa a lógica da distância em km

print(f"\nA distância entre os dois locais é {distancia} km!")

"""Dica 1: o tempo necessário para percorrer uma dada distância à velocidade constante é dado pelo quociente entre a distância e a velocidade.
Dica 2: 1 m/s = 3,6 km/h. Atenção às unidades!"""
# Nesse código, inseri a fórmula para converter a velocidade de m/s para km/h, já que a resposta deverá ser dada em km/h. Em seguida, pedi para o usuário informar o tempo estimado em minutos. No cálculo da distância, utilizei a velocidade já em km/h e converti o tempo informado em minutos para horas.