"""
    Operador lógico not
    inverte expressões 
    True -> False
    False -> True
"""

senha = input('senha: ')

if not senha: #inversão de expressão
    print("Você não digitou nada.")
else:
    print('logado')
