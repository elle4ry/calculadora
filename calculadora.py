#!/usr/bin/env python3

# Calculadora

continuar = True

while continuar:
    print("\nBem-vindo(a) à calculadora!")
    calculo = input("Que tipo de operação você deseja fazer? (soma, subtração, multiplicação, divisão): ")
    case = calculo.lower()

    if case == "soma":
        numeroUM = float(input("Digite o primeiro número: "))
        numeroDOIS = float(input("Digite o segundo número: "))
        soma = numeroUM + numeroDOIS
        print("O resultado da soma é:", soma)

    elif case == "subtração":
        numeroUM = float(input("Digite o primeiro número: "))
        numeroDOIS = float(input("Digite o segundo número: "))
        subtracao = numeroUM - numeroDOIS
        print("O resultado da subtração é:", subtracao)

    elif case == "multiplicação":
        numeroUM = float(input("Digite o primeiro número: "))
        numeroDOIS = float(input("Digite o segundo número: "))
        multiplicacao = numeroUM * numeroDOIS
        print("O resultado da multiplicação é:", multiplicacao)

    elif case == "divisão":
        numeroUM = float(input("Digite o primeiro número: "))
        numeroDOIS = float(input("Digite o segundo número: "))
        if numeroDOIS != 0:
            divisao = numeroUM / numeroDOIS
            print("O resultado da divisão é:", divisao)
        else:
            print("Erro: divisão por zero não é permitida.")

    else:
        print("Operação inválida. Tente novamente.")

    resposta = input("\nDeseja realizar outra operação? Digite 'sim' ou 'não': ")

    if resposta.lower() == "não":
        continuar = False
    elif resposta.lower() != "sim":
        print('Resposta inválida. Digite "sim" ou "não".')

else:
    print("\nVocê saiu da calculadora.")
