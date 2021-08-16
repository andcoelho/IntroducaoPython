#Aula 010 - Comparações múltiplas

"""benefício para maiores de idade (maior que  18
menor que 70)
"""

idade = int(input("Digite sua idade: "))

if idade >18:
    if idade < 70:
        print("Você pode receber o benefício")
    else:
        print("Você não pode receber o benefício")
else:
    print("VocÊ não pode receber o benefício")

"""
programa fico muito extenso e complexo
Para compactar, utilizar comparações múltiplas

Pode colocar por exemplo: 18 <= idade < 70
1 < a < 5
1 < a > 5
1 <= a <= 5
etc.
(1 < 3) < 2
O programa irá imprimir True, pois 1 < 3 é correto, e
na variável booleana, True é 1, logo True < 2
pois: True < 2 == 1 < 2

Analogamente: (1 < 3) < 1 == False
Pois 1 < 3 será True, logo 1
Dessa forma, 1 não pode ser maior que 1, imprimindo False.

Pode ser escrito em cadeia:
1 < 3 < 5 < 6 < 7 < 9 < 10 : True
1 < 3 < 5 < 6 < 7 < 9 < 6  : False
"""

idade = int(input("Digite sua idade: "))

if 18 <= idade < 70:
    print("Você pode receber o benefício")
else:
    print("Você não pode receber o benefício")
