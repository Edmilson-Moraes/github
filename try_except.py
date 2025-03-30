"""
Introdução ao try/except
    O bloco try/except é uma estrutura de tratamento de exceções em Python. 
    Ele permite que você execute um bloco de código e, se ocorrer um erro (exceção), 
    você pode lidar com esse erro de maneira controlada, evitando que o programa seja interrompido abruptamente.
    
    Sintaxe básica:
        try:
            # Código que pode gerar uma exceção
        except TipoDeExcecao:
            # Código para lidar com a exceção
        else:
            # Código a ser executado se não houver exceção
        finally:
            # Código a ser executado independentemente de haver ou não exceção
"""
# Exemplo básico de uso do try/except
def exemplo(): # função apenas pra exemplificar o uso do return
    try:
        numero_1 = int(input('Digite o primeiro número: '))
        numero_2 = int(input('Digite o segundo número: '))
        print(f'A soma dos números é: {numero_1 + numero_2}')
        return
    except ValueError:
        print("Erro: Você deve digitar apenas números inteiros.")
        return
    finally:
        print("Fim do programa.")
    print("não será executado devido ao return(retorna sobre escopo superior de uma função )")
exemplo()
# O bloco finally é executado independentemente de ocorrer ou não uma exceção.
# Isso é útil para liberar recursos ou realizar ações de limpeza.
# Diferentemente do print("Fim do programa."), que só é executado se não houver erro.
"""
O finally é útil em situações onde você precisa garantir que algo aconteça, mesmo que:

    Uma exceção não tratada ocorra.
    O programa seja interrompido por um return, break ou erro grave.
    Haja necessidade de "limpeza" (ex.: fechar arquivos, liberar recursos).
"""
