"""
Exercicio

Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}

Se nada for digitado em nome ou idade:
    exibe "Desculpe, você deixou campos vazios."
        """

nome = input("digite seu nome: ")
idade = input("digite sua idade: ")

if nome.strip() and idade.isdecimal():
    print(f"Seu nome é: {nome}")
    # Exibe o nome invertido utilizando slicing com passo negativo
    print(f"Seu nome invertido é {nome[::-1]}", f"\nseu nome contém espaço." if " " in nome else "Seu nome não contém espaço."
          f"\nSeu nome contém {len(nome)} letras." f"\nA primeira letra do seu nome é {nome[0]}" f"\nA ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")
