"""
Programa 1:
Faça um programa que peça as 4 notas bimestrais e mostre a média
"""

"""
Programa 2:
Faça um programa que pergunte quanto você ganha por hora e número
de horas trabalhas
Calcule e mostre o total do seu salário no referido mês
"""

print("Programa 1: ")
x = int(input("Qual sua nota em matemática? "))
y = int(input("Qual sua nota em física? "))
w = int(input("Qual sua nota em Química? "))
z = int(input("Qual sua nota em biologia? "))
print("Sua média nesse bimestre é:", (x+y+w+z)/4)

print("Programa 2: ")
num = int(input("Quanto você ganha por hora? "))
num2 = int(input("Quantas horas você trabalha? "))
num3 = int(input("Quantos dias ao mês você trabalha? "))

print("Seu salário é: ", num*num2*num3, "reais")
