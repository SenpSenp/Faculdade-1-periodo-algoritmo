#Baseado  no  ano  e  peso  do  modelo  de  um  automóvel,  o  estado  de  Nova  Jersey
#determina a sua classe de peso e taxa de registro usando a seguinte tabela:
#Ano do modelo Peso Classe Taxa de registro
#Menos de 1200 kg 1 16,50
#de 1200 a 1700 kg 2 25,50
#1970 ou antes
#Mais de 1700 kg 3 46,50
#Menos de 1200 kg 4 27,00
#de 1200 a 1700 kg 5 30,50
#1971 a 1979
#Mais de 1700 kg 6 52,50
#Menos de 1600 kg 7 19,501980 ou depois
#1600 kg ou mais 8 55,50
#Usando esta informação, escreva um programa que receba o ano e o peso do modelo
#de um automóvel e calcule e imprima a classe de peso e a taxa de registro para o
#carro.

ano = int(input("Qual ano do seu carro? "))
peso = int(input("Quantos kg pesa seu carro? "))

if ano <=1970:
    if peso <1200:
        print("Classe 1, taxa de 16,50")
    else:
        if peso <= 1700:
            print("classe 2, taxa de 25,50")
        else:
            if peso > 1700:
                print("CLasse 3, taxa de 46,50")
    if ano <1980:
        if peso <1200:
            print("Classe 4, taxa de 27,00")
else:
    if peso <= 1700:
            print("classe 5, taxa de 30,50")
    else:
        if peso > 1700:
            print("CLasse 6, taxa de 52,50")
if ano >= 1980:
    if peso <1600:
        print("Classe 7, taxa de 19,50")
else:
    if peso >= 1600:
            print("classe 8, taxa de 55,50")
