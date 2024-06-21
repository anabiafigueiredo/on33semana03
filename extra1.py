#Crie um programa que pede ao usuário para inserir dois números e tente dividir o primeiro pelo segundo.

numerador = int(input("Digite um número: "))
denominador = int(input("Digite mais um número: "))

try:
    resultado = numerador / denominador
    print(f"O resultado da divisão do primeiro e o segundo número é {resultado}")

except ZeroDivisionError:
    print("Não é possível fazer divisão por zero")




    

