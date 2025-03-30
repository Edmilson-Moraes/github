"""
    Operador lógico or
Se qualquer valor for considerado verdadeiro, então a expressão inteira será avaliada naquele valor    """


senha = input('Senha: ') or 'Sem senha' # o valor que for True será executado
print(senha)

