import time, os, json, re

if os.path.exists("agenda.json"):
    with open("agenda.json", "r") as f:
        agenda_telefonica = json.load(f)
else:
    agenda_telefonica = {}


def mostrar_menu():
    print("Escolha uma das opções abaixo:\n" \
        "1 - Inserir um novo contato\n" \
        "2 - Remover um contato\n" \
        "3 - Listar contatos\n" \
        "4 - Sair")

def inserir_contato():
    #inserção no dicionario
    nome = input("Digite o nome:")
    telefone = input("Digite o telefone (DD) 9XXXX-XXXX:")
    if nome in agenda_telefonica.keys():
        print("Nome já existente!")
    else:
        while True:
            if re.fullmatch(r"\(\d{2}\) 9\d{4}-\d{4}", telefone):
                agenda_telefonica[nome] = telefone
                print("Contato inserido com sucesso!")
                break
            else:
                print("Número fora do padrão!")
                telefone = input("Digite o telefone (DD)-9XXXX-XXXX:")

def remover_contato():
    nome = input("Digite o nome:")
    if nome in agenda_telefonica.keys():
        del agenda_telefonica[nome]
        print("Contato removido com sucesso!")
    else:
        print("Nome inexistente!")

def listar_contatos():
    print("Contato" + " " * 8  + "|" + "Telefone")
    print("-" * 30)

    for chave, valor in agenda_telefonica.items():
        tam = 15 - len(chave)
        print(chave + " "*tam  + "|" +  valor)

def salvar_dados_no_arquivo():
    with open("agenda.json", "w") as f:
        json.dump(agenda_telefonica, f)
    
while (True):
    mostrar_menu()
    opcao = int(input(""))

    if opcao == 1:
        inserir_contato()
    elif opcao == 2:
        remover_contato()
    elif opcao == 3:
        listar_contatos()
    elif opcao == 4:
        salvar_dados_no_arquivo()
        break
    else:
        print("Opção Inválida!")
    
    time.sleep(3)
    os.system("clear")