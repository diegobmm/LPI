#Entrada de Dados
salario = float(input("Digite o salário:"))
quant_libras = float(input("Digite a quantidade de libras:"))

#Processamento de Dados
if quant_libras < 50:
    quit("Quantidade muito pequena inferior ao mínimo!")

investimento_mensal = salario * 0.30
if salario >= 5000:
    investimento_mensal *= 1.05

valor_total = quant_libras * 7.20
total_meses = valor_total / investimento_mensal

#Saida de Dados
print("Total de meses de trabalho é:",total_meses)
