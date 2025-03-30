a = 'AAA'
b = 'BBB'
c = 'CCC'

texto = ('a = {}, b = {}, c = {}')
string = texto.format(a, b, c)
print(string)

#coerção = conversão de um tipo de dado para outro
texto = ("1")
conversao = (int(texto))

print(texto, type(texto))
print(conversao, type(conversao))
