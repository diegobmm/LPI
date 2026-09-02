```python
contas_acima_200 = 0
maior_conta = None
pessoas_maior_conta = None
total_valor_contas = 0
total_contas = 0

while True:
    opcao = int(input("1 - Fechar conta de uma mesa\n"
                      "2 - Encerrar expediente\n"
                      "Digite uma opção: "))

    if opcao != 1 and opcao != 2:
        print("Opção inválida! Tente novamente.")
        continue  # Retorna para o início do loop e solicita novamente a opção

    if opcao == 2:
        break

    else:
        quantidade_pessoas = int(input("Digite a quantidade de pessoas na mesa: "))
        while quantidade_pessoas <= 0:
            quantidade_pessoas = int(input(
                "Valor inválido! Digite uma quantidade positiva de pessoas: "
            ))

        valor_consumido = float(input("Digite o valor total consumido pela mesa: "))
        while valor_consumido <= 0:
            valor_consumido = float(input(
                "Valor inválido! Digite um valor positivo para o consumo: "
            ))

        consumo_por_pessoa = valor_consumido / quantidade_pessoas

        if consumo_por_pessoa > 200:
            contas_acima_200 += 1

        if maior_conta is None or valor_consumido > maior_conta:
            maior_conta = valor_consumido
            pessoas_maior_conta = quantidade_pessoas

        total_valor_contas += valor_consumido
        total_contas += 1

media_por_conta = total_valor_contas / total_contas

print("\n--- RESUMO DO EXPEDIENTE ---")
print("a) Contas com consumo por pessoa superior a R$ 200,00:", contas_acima_200)
print("b) Pessoas na mesa que apresentou a maior conta:", pessoas_maior_conta)
print("c) Gasto médio por conta fechada: R$", media_por_conta)
```
