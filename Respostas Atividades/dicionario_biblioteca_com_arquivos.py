import pprint
import os
import time
import json

if os.path.exists("arquivo_biblioteca.json"):
    with open("arquivo_biblioteca.json", "r") as arquivo:
        biblioteca = json.load(arquivo)
else:
    biblioteca = {
    "Dom Quixote": 30,
    "1984": 50,
    "O Pequeno Príncipe": 48,
    "Harry Potter e a Pedra Filosofal": 67,
    "O Senhor dos Anéis": 23,
    "Capitães da Areia": 51,
    "A Menina que Roubava Livros": 33 }

emprestimos = {}
total_livros_emprestados = 0
while True:
    pprint.pprint(biblioteca)
    livro_desejado = input("Digite o livro desejado:")
    if livro_desejado == "sair":
        break

    quant = int(input("Digite a quantidade:"))

    if livro_desejado in biblioteca.keys():
        if biblioteca[livro_desejado] >= quant:
            biblioteca[livro_desejado] -= quant

            total_livros_emprestados += quant
            if livro_desejado not in emprestimos.keys():
                emprestimos[livro_desejado] = quant
            else:
                emprestimos[livro_desejado] += quant

            print("Livro emprestado com sucesso!")
        else:
            print("Quantidade insuficiente !")
    else:
        print("O livro não existe na biblioteca!")

    time.sleep(2)
    os.system("clear")


with open("arquivo_biblioteca.json", "w") as arquivo:
    json.dump(biblioteca, arquivo)

