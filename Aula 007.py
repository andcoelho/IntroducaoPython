"""
Aula 007 - Funções input e put
"""
"""
imput - o usuário define a viarável
imput imprime uma mensagem na tela, e espera uma resposta do usuário.
"""

"""
modelo:
x = input("Digite um número: ")
"""

""" ao comandar para imprimir x, irá imprimir o input
O programa entende x como uma letra, e não como número.
Para passar para valor de número de inteiro
x = int(x)
"""
#Programa 1
num = int(input("Digite o número de cachorros: "))
print("eu tenho", num," cachorros")

#Programa 2
num = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))

print(num, "+", num2, "=", num + num2)
print(num, "-", num2, "=", num - num2)
print(num, "x", num2, "=", num*num2)
print(num, "//", num2, "=", num // num2)
