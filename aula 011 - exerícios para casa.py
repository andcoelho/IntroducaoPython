#### aula 011 - exercícios casa

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

if num <= 1000:
    print(num//10,"centenas")
elif num <= 100:
    print(num//10, "dezenas")
elif num <= 10:
    print(num//10, "unidades")



else:
    print("numero inválido, only less than 1000")  
