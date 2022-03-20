#Escreva  um  programa  para  calcular  e  mostrar  o  salário  semanal  de  uma  pessoa,
#determinado  pelas  condições  que  seguem.  Se  o  número  de  horas  trabalhadas  for
#inferior  ou  igual  a  40,  a  pessoa  recebe  R$15,00  por  hora,  senão  a  pessoa  recebe
#R$600,00 mais R$21,00 para cada hora trabalhada acima de 40 horas. O programa
#deve pedir o número de horas trabalhadas como entrada e deve dar o salário como
#saída.

hora = int(input("Quantas horas você trabalha? "))
hora40 = hora-40
salario = 15*hora
salario40 = 600+ (21*hora40)

if hora <=40:
    print(f"Seu salário é de {salario}")
if hora > 40:
    print(f"Seu salário é de {salario40}")