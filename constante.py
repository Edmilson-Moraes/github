"""
Constante = "Variáveis que não mudam de valor durante a execução do programa"
# Exemplo de uso:
PI = 3.14
NOME = "Python"
TAXA_DE_JUROS = 0.05
# As constantes são geralmente escritas em letras maiúsculas para diferenciá-las das variáveis comuns.
# Exemplo de uso:
def calcular_area_circulo(raio):
    return PI * (raio ** 2)
# Exemplo de uso:
def calcular_juros(principal, tempo):
    return principal * (1 + TAXA_DE_JUROS) ** tempo 
"""

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local atual do carro na estrada

RADAR_1 = 60 # velocidade máxima permitida no radar 1
LOCAL_1 = 100 # local do radar 1 na estrada
RADAR_RANGE = 1 # distância em km do radar
# Verifica se o carro está acima da velocidade permitida
if velocidade > RADAR_1:
    print("Você foi multado por excesso de velocidade!")
    print(f"Você estava a {velocidade} km/h, e a velocidade máxima permitida era {RADAR_1} km/h.")
else:
    print("Você não foi multado por excesso de velocidade.")
# Verifica se o carro passou pelo radar
if local_carro >= LOCAL_1 - RADAR_RANGE and local_carro <= LOCAL_1 + RADAR_RANGE:
    print("Você passou pelo radar!")
else:
    print("Você não passou pelo radar.")
# O código acima verifica se o carro está acima da velocidade permitida e se passou pelo radar.
