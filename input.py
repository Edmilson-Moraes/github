numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')

verificacao = numero_1.isdecimal(), numero_2.isdecimal()

if verificacao == True:
    int_numero_1 = int(numero_1)
    int_numero_2 = int(numero_2)
    print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
else:
    print("Não foi possível fazer o cáculo")

