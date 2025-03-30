"""
interpolação básica de strings
s - string
d e i - inteiro
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.9876377
variavel = '%s, o preço é R$%.3f' %(nome, preco)

print(f"{variavel}")
print(f"{nome: >10}")# direita
print(f"{nome: <10}")# esquerda
print(f"{nome: ^10}")# centro
print(f"{nome:$^10}")# centro com caractere especial
print(f"{nome:$>10}")# direita com caractere especial
