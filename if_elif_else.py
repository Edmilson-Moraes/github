"""
if, elif e else
Estruturas condicionais em Python. 
"""

entrada = input('Você quer "entrar" ou "sair"? ') # Entrada do usuário

if entrada == "entrar": # Verifica se a entrada é "entrar"
    print("Você entrou no sistema.") # Mensagem de sucesso 
elif entrada == "sair": # Verifica se a entrada é "sair" \ não pode estar sozinha
    print("Você saiu do sistema.")
elif entrada == "sair":
    pass # Não faz nada, apenas passa para o próximo bloco
else: # Se nenhuma das condições anteriores for verdadeira, executa este bloco
    print('Você não digitou "entrar" ou "sair".') # Mensagem de erro
 