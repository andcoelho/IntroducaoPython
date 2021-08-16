#Aula 011 - exerícios

"""
Faça um programa que leia três números e mostre-os
em ordem decrescente.
"""

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a > b > c:
    print(a, b, c)
elif a > c > b:
    print(a, c, b)
elif b > a > c:
    print(b, a, c)
elif b > c > a:
    print(b, c, a)
elif c > a > b:
    print(c, a, b)
else:
    print(c, b, a)

""" Caso os números sejam iguais, o programa buga
necessário colocar não apenas o maior
mas sim o maior ou igual ( => )
"""

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a >= b >= c:
    print(a, b, c)
elif a >= c >= b:
    print(a, c, b)
elif b >= a >= c:
    print(b, a, c)
elif b >= c >= a:
    print(b, c, a)
elif c >= a >= b:
    print(c, a, b)
else:
    print(c, b, a)

#Exercícios para casa!

"""
PROGRAMA 1
Faça um programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os tempos no plural a colocação do "e", da vírguula entre outros. exemplo:

    326 = 3 centenas, 2 dezenas e 6 unidades
    12 - 1 dezena e 2 unidades.

Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311
111, 25, 20, 10, 21, 11, 1, 7, 16

----------
PROGRAMA 2
Faça um programa que leia três númerso e mostre o maior o menor deles.
"""
print("programa 1")
num = int(input("Digite o número"))

if num < 1000:
    print(num//10, "dezena")

else:
    print("numero inválido, only less than 1000")  

