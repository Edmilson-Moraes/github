def exemplo():
    try:
        numero = int(input("Digite um número: "))
        print(10 / numero)
    except ValueError:
        print("Erro: Digite um número válido.")
        return  # Válido dentro da função
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
        return
    print("Fim do programa.")

exemplo()  # Chama a função