#Efetuar a leitura de uma nota e, se o valor for maior ou igual a 60, imprimir na tela
#"APROVADO", se for menor, imprimir reprovado. Testar ainda se o valor lido foi
#maior do que 100 ou menor do que zero. Neste caso, imprimir "NOTA
#INVÁLIDA".

nota = float(input("Qual sua nota? "))

if nota < 0 or nota > 100:
    print("Nota inválida")
else:
    if nota < 60:
        print("Reprovado")
    else:
        if nota >= 60:
            print("Aprovado")