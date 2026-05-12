# Atividade de Laboratório - Ovos Caipira (Resposta)

#Entrada de Dados
quant_ovos_brancos = int(input("Digite a quantidade de ovos brancos:"))
quant_ovos_vermelhos = int(input("Digite a quantidade de ovos vermelhos:"))

#Processamento de Dados
cartela_ovos_brancos = quant_ovos_brancos // 30
bandejas_ovos_vermelhos = quant_ovos_vermelhos // 12

sobra_ovos_brancos = quant_ovos_brancos % 30
sobra_ovos_vermelhos = quant_ovos_vermelhos % 12

quant_omeletes = sobra_ovos_brancos // 3
quant_ovos_mexidos = sobra_ovos_vermelhos // 2

resto_final_ovos_branco = sobra_ovos_brancos % 3
resto_final_ovos_vermelhos = sobra_ovos_vermelhos % 2

Valor_total_vendas = (cartela_ovos_brancos * 42.5) + \
                     (bandejas_ovos_vermelhos * 17.5) + \
                     (quant_omeletes * 6.5) + \
                     (quant_ovos_mexidos * 8.0) + \
                     (resto_final_ovos_branco * 0.25) + \
                     (resto_final_ovos_vermelhos * 0.40)
#Saída de Dados

print("Quantidade de cartelas vendidas de ovos branco:", cartela_ovos_brancos)
print("Quantidade de bandejas vendidas de ovos vermelhos:", bandejas_ovos_vermelhos)
print("Quantidade de omeletes vendidos:", quant_omeletes)
print("Quantidade de pão com ovo mexido vendidos:", quant_ovos_mexidos)
print("Total arrecadado com todas as vendas do dia:", Valor_total_vendas)