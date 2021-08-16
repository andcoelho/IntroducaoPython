"""
Faça um programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão: 1, 5, 10, 20, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes
na Máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece
    duas notas de 100, uma de 50 e uma nota de 5 e uma de 1;

    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornnece
    Três notas de 100, uma nota de 50, quatro notas de 10,
    Uma nota de 5 e quatro notas de 1.
"""

saque = int(input("Olá!\nBem vindo ao Banco K \nO saque mínimo é de 10 reais \nO saque máximo é de 600 reais \nDigite a quantidade do saque: "))

if 10 <= saque <= 600:
    valor1 = saque//100
    rest1 = saque%100
    print("O valor do saque é:", saque, "Reais \nVocê receberá", valor1, "notas de cem")
    if rest1 > 0:
        valor2 = rest1//50
        rest2 = rest1%50
        print(valor2,"notas de cinquenta")
        if rest2 > 0:
            valor3 = rest2//20
            rest3 = rest2%20
            print(valor3, "notas de vinte")
            if rest3 >0:
                valor4 = rest3//10
                rest4 = rest3%10
                print(valor4, "notas de dez")
                if rest4>0:
                    valor5 = rest4//5
                    rest5 = rest4%5
                    print(valor5, "notas de cinco")
                    if rest5>0:
                        valor6 = rest5//1
                        rest6 = rest5%1
                        print(valor6, "notas de um")

else:
    print("Esse valor não pode ser sacado \nReinicie o processo")
