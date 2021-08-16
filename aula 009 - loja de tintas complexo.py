#Loja de tintas complexo - Aula 009

"""
3)
Faça um programa para uma loja de tintas(mais complexo)

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$80,00 ou
em galões de 4 litros, que custam R$25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.


Acrescente 10% de folga e sempre arredonde valores para cima, isto é,
considere latas cheias
"""

area = int(input("Quantos metros quadrados você irá pintar?"))
litros = area/6

if litros <=4:
    print("Você irá gastar", litros,".\n É necessário comprar 1 lata de 4 litros \nValor total: 25 reais")

if litros >4:
    if litros <=18:
        galão = litros//4
        if litros%4 >0:
            galão = galão +1
            preço = galão*25
            print("Você irá gastar", litros, "litros. \nÉ necessário comprar", galão, "galões pelo valor de", preço, "ou comprar 1 lata de 18 litros por 80,00 reais")

if litros >18:
    print("Você vai gastar", litros, "litros")
    lata = litros//18
    print("Você vai comprar", lata,"latas")
    rest1 = litros%18
    if rest1==0:
        print("O preço é:",(lata*80), "reais")
    else:
        galao = rest1//4
        if rest1%4 >0:
            galao = galao +1    
            preço = (lata*80) + (galao*25)
            print("e", galao, "galões")
            print("O preço é", preço,"reais")
    
    


    
