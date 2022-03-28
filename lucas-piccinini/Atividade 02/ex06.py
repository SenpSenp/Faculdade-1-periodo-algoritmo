#Ler um número e informar se ele é positivo, negativo ou neutro (zero).

numero = int(input("Digite um número: "))

if numero > 0:
    print("Número positivo")
else:
    if numero == 0:
        print("Numero neutro")
    else:
        if numero < 0:
            print("Numero negativo")