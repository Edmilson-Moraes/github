"""
Flag = marcar um local
None = não valor
is e is not = é ou não é(tipo, valor, identidade)
id = Identidade
"""
# Define a condição inicial como False
condicao = False

# Variável para verificar se passou no bloco if, inicialmente definida como None
passou_no_if = None

# Verifica a condição
if condicao:
    # Se a condição for verdadeira, atualiza a variável e executa uma ação
    passou_no_if = True
    print("Faça algo!")
else:
    # Caso contrário, executa outra ação
    print('Não faça algo!')

# Verifica se a variável passou_no_if ainda é None
print(passou_no_if, passou_no_if is None)

# Verifica se a variável passou_no_if não é None
print(passou_no_if, passou_no_if is not None)
