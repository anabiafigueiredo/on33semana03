#Crie uma função que soma dois números fornecidos pelo usuário. 

def soma(a,b):
    resultado = a + b
    return resultado

entrada1 = input("Digite um número: ")
entrada2 = input('Digite outro número: ')

try:
    numero1 = float(entrada1)
    numero2 = float(entrada2)

    resultado = soma(numero1, numero2)
    print(f'O resultado da soma dos números {numero1} e {numero2} é {resultado}')

except ValueError:
    print('erro: insira números válidos')    
