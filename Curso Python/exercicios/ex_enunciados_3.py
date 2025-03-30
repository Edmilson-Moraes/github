"""
Faça um programa que peça o peimeiro nome do usuário. Se o nome tiver 4 letras ou 
menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu nome: ')

print(f"Seu nome ({nome}) é curto" if len(nome) <= 4 else f"Seu nome ({nome}) é normal" if len(nome) <=6 else\
       f"Seu nome ({nome}) é muito grande")
