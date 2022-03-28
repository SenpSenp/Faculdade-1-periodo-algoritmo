#Efetuar a leitura de uma nota e, se o valor for maior ou igual a 60, imprimir na tela "APROVADO",
#se for menor, imprimir reprovado.

nota = float(input("Qual sua nota? "))

if nota < 60:
    print("Reprovado")
else:
    if nota >= 60:
        print("Aprovado")