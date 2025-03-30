def cor(valor): #
    cores = {
        "vermelho": "red", 
        "verde": "green",
        "azul": "blue",
    } # dicionario 
    return cores.get(valor.lower(), "cor não reconhecida") # 

pergunta = input("qual a cor?")
resultado = cor(pergunta)
print(resultado)