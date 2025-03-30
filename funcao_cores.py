def cor(valor):
    valor = valor.lower() # converte para minúsculas
    if valor == "vermelho":
        return "red"
    elif valor == "verde":
        return "green"
    elif valor == "azul":
        return "blue"
    else:
        return "Cor não reconhecida"

pergunta = input("Qual a cor? ")
resultado = cor(pergunta)
print(resultado) 