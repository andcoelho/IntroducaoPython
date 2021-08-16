#Aula 009 - Exercício 1

"""
Faça um programa que peça dois números e imprima o maior deles.
"""

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if num1> num2:
    print("\nO número", num1,"é maior que o número", num2)
if num1 == num2:
        print("\nO número_", num1,"é igual ao número", num2)
if num1<num2:
    print("\nO número", num2, "é maior que o número_", num1)

#Gabarito
print("\nResolução pelo gabarito")

num1 = int(input("\nDigite o primeiro numero: "))
num2 = int(input("\nDigite o segundo numero: "))

if num1 >= num2:
    print(num1)
else:
    print(num2)
