#Informar o número do mês do ano e mostrar o nome do mês por extenso. Caso o
#número do mês não exista, exibir a mensagem "Mês inválido".

mes = int(input("Digite o número de um mes: "))

if mes == 1:
    print("Janeiro")
if mes == 2:
    print("Fevereiro")
if mes == 3:
    print("Março")
if mes == 4:
    print("Abril")
if mes == 5:
    print("Maio")
if mes == 6:
    print("Junho")
if mes == 7:
    print("Julho")
if mes == 8:
    print("Agosto")
if mes == 9:
    print("Setembro")
if mes == 10:
    print("Outubro")
if mes == 11:
    print("Novembro")
if mes == 12:
    print("Dezembro")
if mes < 1 or mes > 12:
    print("Mes invalido")