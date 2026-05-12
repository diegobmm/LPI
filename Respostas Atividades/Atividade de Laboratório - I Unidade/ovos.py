# Atividade de Laboratório - Ações (Resposta)

#Entrada de Dados
total_ações = int(input("Digite o total de ações:"))
custo_lote = float(input("Digite o custo de um lote de ações:"))
custo_fração = float(input("Digite o custo da ação fracionada:"))

# Processamento de Dados
quant_lotes = total_ações // 100
quant_ações_fracionadas = total_ações % 100
valor_total=quant_lotes*custo_lote+quant_ações_fracionadas*custo_fração
if quant_lotes>=5:
    valor_descontado= valor_total*0.05
else:
    valor_descontado= 0
valor_do_IOF=(valor_total-valor_descontado)*0.015
valor_do_cliente=valor_total-valor_descontado+valor_do_IOF
# Saída de Dados
print("A quantidade de lotes comprados:", quant_lotes)
print("A quantidade de ações fracionadas:", quant_ações_fracionadas)
print("O custo total das ações:", valor_total)
print("O valor do desconto (se houver):", valor_descontado)
print("O valor do IOF (1,5%):", valor_do_IOF)
print("Valor final a ser pago pelo cliente:", valor_do_cliente)