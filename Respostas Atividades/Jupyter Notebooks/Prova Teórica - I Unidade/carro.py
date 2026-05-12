#Entrada de Dados
valor_carro = float(input("Digite o valor do carro:"))
tipo_carro = input("Tipo do carro:") #Vamos assumir que um dos três tipos serão digitados

#Processamento de Dados
IPI = 0.11 * valor_carro
if tipo_carro == "popular":
    IPI = IPI * 0.75
elif tipo_carro == "SUV":
    IPI = IPI * 0.90
else:
    IPI = 0

valor_final = valor_carro + IPI

if tipo_carro == "elétrico" and valor_carro < 120000:
    valor_final = valor_final - 5000

#Saída de Dados
print("Valor final:", valor_final)
