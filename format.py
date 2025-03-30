"""
Formatação de strings com o método format
"""

a = "AAA" # 0
b = "BBB" # 1
c = "1.1" # 2

string = 'b={1} a={0} a={0} a={0} c={nome3}' # os números indicam o índice
formato = string.format(
    a,b,nome3=c) # Após o primeiro parâmetro ser nomeado, os próximos também precisam ser

nome = "edmilson"
idade = "29"
texto = "Meu nome é {1} e eu tenho {0} anos.".format(nome,idade) #é possível organizar a ordem
# dos elementos através de números dentro das chaves
print(texto)