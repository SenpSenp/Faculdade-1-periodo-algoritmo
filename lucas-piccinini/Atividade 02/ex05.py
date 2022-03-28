#Ler um número inteiro e testar se o valor lido termina com 0 (divisível por 10). Em
#caso positivo, exiba a metade deste número. Caso contrário, exibir a mensagem "O
#número digitado não termina com 0".

numero = int(input("Digite um número inteiro: "))
resto = numero % 10

if resto == 0:
    print(f"{numero/2:.2f}")
else:
    print("O numero digitado não termina com 0")