#Escreva  um  programa  que  receba  dois  números  reais  e  um  código  de  seleção  do
#usuário.  Se  o  código  digitado  for  1,  faça  o  programa  adicionar  os  dois  números
#previamente  digitados  e  mostrar  o  resultado;  se  o  código  de  seleção  for  2,  os
#números devem ser multiplicados; se o código de seleção for 3, o primeiro número
#deve  ser  dividido  pelo  segundo.  Se  nenhuma  das  opções  acima  for  escolhida,
#mostrar "Código inválido".

num1 = float(input("Digite um número real: "))
num2 = float(input("Digite mais um número real: "))
codigo = int(input("Digite o código, entre 1 e 3:"))

if codigo == 1:
    print(f"{num1 + num2}")
else:
    if codigo == 2:
        print(f"{num1 * num2:}")
    else:
        if codigo == 3:
            print(f"{num1 / 2}")
        else:
            print("Código inválido")