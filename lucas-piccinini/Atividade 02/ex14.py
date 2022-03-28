#Desenvolva um algoritmo que leia o nome de um aluno, suas notas em 2 provas e
#em  um  trabalho  (todas  com  valores  entre  0  e  10)  e  sua  frequência,  definindo  e
#imprimindo  se  ele  foi  aprovado,  reprovado  ou  se  fará  prova  final.  O  aluno  será
#reprovado se faltou mais de 15 aulas. Será aprovado se não for reprovado por falta
#e sua média for maior que 6,0. Caso tenha média menor, deverá fazer prova final.
#O  cálculo  da  média  deve  ser  feito  com  peso  3  para  a  primeira  prova,  5  para  a
#segunda prova e 2 para o trabalho.

nome = input("Qual seu nome? ")
prova_1 = float(input(f"{nome}, Qual a nota da sua prova 1? "))
prova_2 =  float(input(f"{nome}, Qual a nota da sua prova 2? "))
trabalho =  float(input(f"{nome}, Qual a nota de seu trabalho? "))
faltas = int(input(f"{nome}, Quantas faltas você teve? "))
media = ((prova_1 * 3) + (prova_2 * 5) + (trabalho * 2)) / 10

if faltas > 15:
    print("REPROVADO")
else:
    if media > 6:
        print("APROVADO")
    else:
        print("Você deve fazer a prova final")