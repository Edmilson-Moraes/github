"""
Fatiamento de Strings
    O fatiamento de strings permite acessar partes específicas de uma string, 
    extraindo substrings com base em índices. Ele utiliza a seguinte sintaxe:

        string[inicio:fim:passo]

    - inicio: O índice inicial (inclusivo), ou seja, o índice onde o fatiamento começa. 
              Se omitido, o padrão é 0 (início da string).
    - fim: O índice final (exclusivo), ou seja, o índice onde o fatiamento para. 
           Se omitido, o padrão é o comprimento total da string.
    - passo: O intervalo entre os índices. Um valor positivo percorre a string da esquerda para a direita, 
             enquanto um valor negativo percorre da direita para a esquerda. 
             Se omitido, o padrão é 1 (passo simples).

    Observações:
    - Índices negativos podem ser usados para contar de trás para frente na string.
    - Se o valor de 'inicio' for maior ou igual ao de 'fim' (com passo positivo), o resultado será uma string vazia.
    - O fatiamento não altera a string original; ele retorna uma nova substring.

    Exemplos:
    texto = "Python"
    texto[0:3]       # Retorna 'Pyt' (índices 0, 1 e 2)
    texto[:3]        # Retorna 'Pyt' (equivalente a texto[0:3])
    texto[3:]        # Retorna 'hon' (do índice 3 até o final)
    texto[::2]       # Retorna 'Pto' (caracteres nos índices pares)
    texto[::-1]      # Retorna 'nohtyP' (string invertida)
"""

string = 'Olá mundo'
# Imprime os dois primeiros caracteres da string
print(string[:2])  # Saída: 'Ol'

# Imprime a string a partir do terceiro caractere até o final
print(string[2:])  # Saída: 'á mundo'

# Imprime a string pulando de 2 em 2 caracteres
print(string[::2])  # Saída: 'Oámno'

# Imprime a string a partir do segundo caractere até o índice 100, pulando de 3 em 3 caracteres
# Como o índice 100 é maior que o tamanho da string, o fatiamento será feito até o final da string
print(string[1:100:3])  # Saída: 'ámn'

