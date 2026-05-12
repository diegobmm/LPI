#Entradas
lado_1 = float(input("Digite o primeiro lado:"))
lado_2 = float(input("Digite o segundo lado:"))
lado_3 = float(input("Digite o terceiro lado:"))

#Processamento e Saída
if lado_1 <=0 or lado_2<=0 or lado_3<=0 :
    quit("Valores inválido!")
if (lado_1 < lado_2 + lado_3) and (lado_2 < lado_3 + lado_1) and (lado_3 < lado_2 + lado_1):
    if lado_1 == lado_2 and lado_2 == lado_3:
        print("Triângulo Equilátero!")
    elif lado_1 != lado_2 and lado_2!=lado_3 and lado_1!=lado_3:
        print("Triângulo Escaleno")
    else:
        print("Triângulo Isósceles")
else:
    print("Não forma triângiulo!")
