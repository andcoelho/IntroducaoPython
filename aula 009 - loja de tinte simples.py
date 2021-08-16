### loja de tinta simples - Aula 009

"""
1)
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$80,00.

Informe ao usuário a quantidade de latas de tinta
a serem compradas e o preço total.
"""

area = int(input("Quantos metros quadrados serão pintados?"))
litros = area/3
latas = litros//18
if litros%18 >0:
    latas = latas +1
preço = latas*80


print("Você irá gastar", litros, "litros, e será necessário comprar", latas, "latas \nO preço total é de", preço, "reais")
