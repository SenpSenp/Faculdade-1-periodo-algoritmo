#Faça um algoritmo que transforme a nota de um aluno em conceito. As notas 10 e
#9 receberão conceito A, as notas 8 e 7 receberão conceito B, as notas 6 e 5 receberão
#conceito C e abaixo de 5 conceito D.

nota = float(input("Digite sua nota aqui: "))

if nota == 10 or nota == 9:
    nota = "A"
else:
    if nota == 8 or nota == 7:
        nota = "B"
    else:
        if nota == 6 or nota == 5:
            nota = "C"
        else:
            nota = "D"
print(nota)
