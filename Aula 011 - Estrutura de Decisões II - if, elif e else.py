#Aula 011 - Estrutura de Decisões II: if, elif e else
"""
Faça um programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2-Segunda, etc.), se digitar outro valor deve aparecer valor
inválido.
"""
print("Programa 1")
dia = int(input("Digite o dia da semana"))

if dia == 1:
    print("domingo")
if dia == 2:
    print("segunda")
if dia == 3:
    print("terça")
if dia == 4:
    print("quarta")
if dia == 5:
    print("quinta")
if dia == 6:
    print("sexta")
if dia == 7:
    print("sabado")
else:
    print("valor inválido")

"""dará erro, só funciona se o número for 7
pois ao digitar qualquer outro número, o else estará
ligado ao último if, logo, imprimirá o outro número
junto a mensagem de "valor inválido"

"""
print("Programa 2")
dia = int(input("Digite o dia da semana"))
verifica = False

if dia == 1:
    print("domingo")
    verifica = True
if dia == 2:
    print("segunda")
    verifica = True
if dia == 3:
    print("terça")
    verifica = True
if dia == 4:
    print("quarta")
    verifica = True
if dia == 5:
    print("quinta")
    verifica = True
if dia == 6:
    print("sexta")
    verifica = True
if dia == 7:
    print("sabado")
    verifica = True

if verifica != True:
    print("entrada inválida")

""" O programa agora funciona
Ao imprimir a váriavel verifica = False,
é necessário que em algum If o verifica seja igual a True
Caso isso não aconteça, o último If entende que Verifica permaneceu False
imprimindo a entrada inválida.

Porém, esse programa não é "elegante", nem eficiente
há muitas repetições.
É necessário deixar o verifica implícita

Facilitando:
Uso do Elif (Se mais alguma coisa)
Pode colocar quantos Elif's quiser
"""
print("Programa 3 (com elif)")
dia = int(input("Digite o dia da semana"))

if dia == 1:
    print("domingo")
elif dia == 2:
    print("segunda")
elif dia == 3:
    print("terça")
elif dia == 4:
    print("quarta")
elif dia == 5:
    print("quinta")
elif dia == 6:
    print("sexta")
elif dia == 7:
    print("sabado")
else:
    print("valor inválido")

"""Outro exemplo"""

print("Programa digite um número 1")
num = int(input("Digite um numero: "))

if num <15:
    print("menor que 15")
if num <20:
    print("Menor que 20")
else:
    print("Ola")

"""Caso o número seja 10,
10 é menor que 15 e menor que 20
logo imprimirá os dois If's
Nesse caso, usar o Elif
"""
print("Programa digite um número 2")
num = int(input("Digite um numero: "))

if num <15:
    print("menor que 15")
elif num <20:
    print("Menor que 20")
else:
    print("Ola")
"""Ao verificar o If como verdadeiro
O programa sequer verifica o Elif





