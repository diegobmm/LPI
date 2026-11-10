import time, os, pickle
from datetime import datetime

# Variáveis globais
reservas = []
nome_arquivo = "reservas.pkl"
TIPOS_QUARTO = ["Pataxó", "Ancestral", "Descobrimento"]
VALOR_QUARTOS = {"Pataxó":100, "Ancestral":180, "Descobrimento":250}
QUARTOS_TOTAIS = {"Pataxó": 10, "Ancestral": 5, "Descobrimento": 3}

def imprimir_reserva_formatada(r):
    responsavel = r['responsavel']
    checkin = r['checkin'].strftime("%d/%m/%Y") 
    checkout = r['checkout'].strftime("%d/%m/%Y")
    tipo_quarto = r['tipo_quarto']
    quantidade = r['quantidade_quartos']
    valor = r['valor']

    print(f"{responsavel:<20} {checkin:<12} {checkout:<12} {tipo_quarto:<15} {quantidade:<6} R$ {valor:>8.2f}")


def carregar_reservas():
    try:
        with open(nome_arquivo, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []  # se o arquivo ainda não existe, retorna lista vazia

def salvar_reservas():
    with open(nome_arquivo, "wb") as f:
        pickle.dump(reservas, f)

def verificar_disponibilidade(checkin_novo, checkout_novo, tipo_quarto, qtd_quartos):
    ocupados = 0
    for r in reservas:
        if r["tipo_quarto"] == tipo_quarto:
            # Se há sobreposição de períodos, somamos os quartos dessa reserva
            if checkin_novo < r["checkout"] and checkout_novo > r["checkin"]:
                ocupados += r["quantidade_quartos"]

    # Calcula quantos ainda restam
    disponiveis = QUARTOS_TOTAIS[tipo_quarto] - ocupados
    if qtd_quartos <= disponiveis:
        return True
    else:
        return False

def cadastrar_reserva():
    print("Cadastrando uma nova reserva..")

    while True:
        responsavel = input("Digite o nome do responsável:").capitalize()
        if responsavel == "":
            print("O nome não pode ser vazio!")
        else:
            break

    # Solicita as datas ao usuário
    while True:
        while True:
            try:
                data_checkin_str = input("Digite a primeira data (dd/mm/aaaa): ")
                data_checkin = datetime.strptime(data_checkin_str, "%d/%m/%Y")
                break
            except ValueError:
                print("Data inválida no checkin!")

        while True:
            try:	
                data_checkout_str = input("Digite a segunda data (dd/mm/aaaa): ")
                data_checkout = datetime.strptime(data_checkout_str, "%d/%m/%Y")
                break 
            except ValueError:
                print("Data inválida no checkout!")
                
        # Calcula a diferença entre as datas
        diferenca = (data_checkout - data_checkin).days
        if diferenca > 0 :
            break
        else:
            print("Data de checkout inferior a de checkin!")

    tipo_quarto = input("Digite o tipo de quarto: Pataxó, Ancestral, Descobrimento:")
    while tipo_quarto not in TIPOS_QUARTO:
        tipo_quarto = input("Digite o tipo de quarto: Pataxó, Ancestral, Descobrimento:")

    while True:
        try:
            quantidade_quartos = int(input("Digite a quantidade de quarto:"))
            break
        except:
            print("Por favor insira um numero válido!")
    
    disponibilidade = verificar_disponibilidade(data_checkin, data_checkout, tipo_quarto, quantidade_quartos)
    if disponibilidade == True:
        nova_reserva = {            
            "responsavel": responsavel,
            "checkin": data_checkin,
            "checkout": data_checkout,
            "tipo_quarto": tipo_quarto,
            "quantidade_quartos": quantidade_quartos,
            "valor": VALOR_QUARTOS[tipo_quarto] * quantidade_quartos * diferenca
        }
        reservas.append(nova_reserva)
        print("Reserva registrada com SUCESSO!")
    else:
        print("Não há vagas disponíveis !")

def consultar_reserva():
    print("Consultando uma nova reserva..")
    responsavel = input("Digite o nome do responsável a buscar:").capitalize()
    for r in reservas:
        if r["responsavel"] == responsavel:
            imprimir_reserva_formatada(r)


def cancelar_reserva():
    print("Cadastrando uma nova reserva..")
    responsavel = input("Digite o nome do responsável a buscar:").capitalize()
    for r in reservas:
        if r["responsavel"] == responsavel:
            reservas.remove(r)
            print("Reserva removida com SUCESSO!")

def listar_reserva():
    print("Listando reservas..")
    print(f"{'Responsável':<20} {'Check-in':<12} {'Check-out':<12} {'Tipo':<15} {'Qtd.':<6} {'Valor':>10}")
    print("-" * 80)
    for r in reservas:
        imprimir_reserva_formatada(r)

    input("\nPressione enter para voltar ao menu.")

def exibir_estatisticas():
    print("Total de Reservas:", len(reservas))
    sum = 0
    for r in reservas: 
        sum +=r["valor"]
    print("Soma Total do Valor das Reservas: R$:", sum)

    reserva_mais_cara = max(reservas, key=lambda r: r["valor"])
    print(f"Reserva mais Cara (R$ {reserva_mais_cara['valor']}) e o seu Responsável ({reserva_mais_cara['responsavel']})")
    reserva_mais_longa = max(reservas, key=lambda r: (r["checkout"]-r['checkin']).days)
    print(f"Reserva mais longa ({(reserva_mais_longa['checkout']-reserva_mais_longa['checkin']).days} dias )e o responsável por ela ({reserva_mais_longa['responsavel']})")


    quartos_por_categoria = {"Pataxó":0, "Ancestral":0, "Descobrimento":0}
    for r in reservas:
        quartos_por_categoria[r["tipo_quarto"]] += r["quantidade_quartos"]
    print(f"Quant. de Quartos alocados por Categorias: Pataxó:{quartos_por_categoria["Pataxó"]}, Ancestral:{quartos_por_categoria["Ancestral"]}, Descobrimento:{quartos_por_categoria["Descobrimento"]}")

    input("\nPressione enter para voltar ao menu.")

def mostrar_menu():
    print("####################################")
    print("########        MENU       #########")
    print("####################################")
    print("1 - Cadastrar uma nova reserva")
    print("2 - Consultar uma nova reserva")
    print("3 - Cancelar uma nova reserva")
    print("4 - Listar todas as reservas")
    print("5 - Exibir Estatisticas")
    print("6 - Sair")

def main():
    os.system("clear")
    #No inicio do programa eu carregarei os dados 
    global reservas
    reservas = carregar_reservas()
    while True:
        mostrar_menu()
        opcao = int(input("Digite uma opção:"))
        if opcao == 1:
            cadastrar_reserva()
        elif opcao == 2:
            consultar_reserva()
        elif opcao == 3:
            cancelar_reserva()
        elif opcao == 4:
            os.system("clear")
            listar_reserva()
        elif opcao == 5:
            os.system("clear")
            exibir_estatisticas()
        elif opcao == 6:
            salvar_reservas()
            break
        else:
            print("Opção inválida!")

        time.sleep(2)
        os.system("clear")

main()