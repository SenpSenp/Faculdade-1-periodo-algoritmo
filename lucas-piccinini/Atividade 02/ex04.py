#Ler um número inteiro e informar se o número lido é par ou impar.

numero = int(input("Digite um número inteiro: "))
resto = numero % 2

if resto == 0:
    print("Numero par")
if resto == 1:
    print("Numero impar")