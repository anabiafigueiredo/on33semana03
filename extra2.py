#Pedir ao usuário para inserir um número inteiro 
#Garanta que a entrada seja realmente um número inteiro.

numero = input('Digite um número: ')

try:
    entra1 = int(numero)
    print('Número recebido com sucesso')

except ValueError:
         print("Erro: insira apenas números inteiros")