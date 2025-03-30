"""
    Dicionario de livros por autor
"""
def livro(valor):
    livros = {
        "tolkien" : "Senhor dos Anéis, Hobbit e Silmarillion",
        "cs lewis" : "Narnia, Cristianismo Puro e Simples"
    }
    valor = valor.lower()
    resultado = livros.get(valor, "Autor não encontrado")
    if resultado != "Autor não encontrado":
        return f"Autor: {valor.capitalize()} - Obras: {resultado}"
    return resultado

autor = input("digite um autor: ")
resultado = livro(autor)
print(resultado)