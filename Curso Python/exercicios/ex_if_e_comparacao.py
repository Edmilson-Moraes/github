"""
desafio: crie um algoritmo que armazene dois digitos do usuário e retorne qual tem o maior valor que o outro.
"""

numero_1 = input("Digite um numero: ")
numero_2 = input("Digite o segundo número: ")

if numero_1 >= numero_2:
    print(f"O primeiro numero: {numero_1} é maior ou igual ao segundo numero: {numero_2}")
else:
    print(f"O segundo numero: {numero_2} é maior ou igual ao primeiro numero: {numero_1}")
