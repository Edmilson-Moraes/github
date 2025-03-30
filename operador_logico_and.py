"""
    Operadores Logicos
    and (e) or (ou) not(não)
    and - todas as condições devem ser verdadeiras
"""

entrada = input ("[E]ntrar  [S]air:\n")
senha_digitada = input("Senha: \n")

senha_permitida= '123456'

if entrada == 'e' and senha_digitada == senha_permitida: # se todas forem True ele executa o bloco
    print('Logado.')
else:
    print('Sair')
