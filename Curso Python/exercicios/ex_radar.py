"""
Crie um algoritmo que leia a velocidade de um carro e diga se ele foi multado ou não.
    Se a velocidade for maior que 60 km/h, imprima "Você foi multado por excesso de velocidade!".
    Caso contrário, imprima "Você não foi multado por excesso de velocidade!".
    O algoritmo deve considerar que o radar está localizado a 100 km da estrada e tem um alcance de 1 km (ou seja, o carro deve passar entre 99 e 101 km para ser considerado multado).

"""

RADAR_1 = 60  # velocidade máxima permitida no radar 1
LOCAL_1 = 100  # local do radar 1 na estrada
RADAR_RANGE = 1  # distância em km do radar

velocidade = float(input("Digite a velocidade do carro (em km/h): ")) 
carro_passou_radar1 = float(input("Digite a localização do carro (em km): "))
perimetro = carro_passou_radar1 >= LOCAL_1 - RADAR_RANGE and carro_passou_radar1 <= LOCAL_1 + RADAR_RANGE

if velocidade > RADAR_1 and perimetro:
    print("Você foi multado por excesso de velocidade!"
    f"\nVocê estava a {velocidade} km/h, e a velocidade máxima permitida era {RADAR_1} km/h.")
else:
    print("Você não foi multado por excesso de velocidade.")