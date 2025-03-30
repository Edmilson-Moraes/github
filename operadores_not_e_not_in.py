"""
Operadores `not` e `not in`

- `not` inverte o valor lógico de uma expressão.
- `not in` verifica se um valor não está presente em uma sequência (como listas, strings ou dicionários).
"""

nome = "Otávio"

print('á' in nome)  # True

# ou

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    posicao = nome.find(encontrar)
    print(f"{encontrar} está em {nome} na posição {posicao}")
else:
    print(f"{encontrar} não está em {nome}")