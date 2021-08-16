#Aula 009 - Estrutura de decisões: If e Else

"""
idade = int(input("Digite sua idade: "))
resp = idade >= 18

print(resp)


Nesse modelo de variável booleana, ele imprime verdade ou falso
"""

#If - condição

idade = int(input("Digite sua idade: "))
resp = idade >= 18

if resp == True:
    print("Você pode beber a vondade")
if resp == False:
    print("Você nao pode beber alcoolicos")

#melhorando 1

idade = int(input("Digite sua idade(1): "))
resp = idade >= 18

if resp:
    print("Você pode beber a vondade")
if resp != True:
        print("Você nao pode beber alcoolicos")

#melhorando 2

idade = int(input("Digite sua idade(2): "))
if idade >= 18:
    print("você pode beber tudo")
if idade <18:
    print("Só água")
if idade >=21:
    print("Você é VIP")
#melhorando 3
#como 21 é maior que 18, é preferível o If dentro do If +18

idade = int(input("Digite sua idade(3): "))
if idade >= 18:
    print("você pode beber tudo")
    if idade >=21:
        print("Você é VIP")
if idade <18:
    print("Só água")

#Melhorando 4
""" Os dois "If" principais estão relacionados
Casa um seja verdadeiro, o outro será falso, e vice-versa
logo, é possível escrever isso de modo a simplificar
"""
idade = int(input("Digite sua idade(4): "))
if idade >= 18:
    print("você pode beber tudo")
    if idade >=21:
        print("Você é VIP")
else: 
    print("Só água")



