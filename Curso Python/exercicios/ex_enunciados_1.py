"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se enste número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input ("digite um número inteiro: ")

if numero.isnumeric():
    numero = int(numero)
    print(f"O número {numero} é par" if numero % 2 == 0 else f"O número {numero} é ímpar")
else:
    print("Você não digitou um número inteiro.")