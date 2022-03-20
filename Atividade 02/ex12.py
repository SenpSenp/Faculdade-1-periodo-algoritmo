#A taxa de juros aplicada em fundos depositados em um banco é determinada pelo
#tempo  em  que  estes  ficam  depositados.  Para  um  banco  em  particular,  a  seguinte
#Tempo em depósito Taxa de juro
#Maior ou igual a 5 anos 0,95
#Menor que 5 anos mas maior ou igual a 4 anos 0,90
#Menor que 4 anos mas maior ou igual a 3 anos 0,85
#Menor que 3 anos mas maior ou igual a 2 anos 0,75
#Menor que 2 anos mas maior ou igual a 1 ano 0,65
#Menor que 1 ano 0,55
#Usando  esta  informação,  escreva  um  programa  que  receba  o  tempo  em  que  os
#fundos foram mantidos em depósito e informe a taxa de juros correspondente.

tempo = int(input("Quanto tempo os fundos foram mantidos? "))

if tempo < 1:
    print("45% de juros")
else:
    if tempo <2:
        print("35% de juros")
    else:
        if tempo <3:
            print("25% de juros")
        else:
            if tempo <4:
                print("15% de juros")
            else:
                if tempo < 5:
                    print("10% de jusros")
                else:
                    if tempo >= 5:
                        print("5% de juros")