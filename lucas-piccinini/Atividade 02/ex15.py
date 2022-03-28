#Faça um algoritmo para verificar e imprimir entre 4 números lidos qual é o menor.

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
num3 = float(input("Digite um terceiro numero: "))
num4 = float(input("Digite um numero final: "))

if num1 < num2 and num1 < num3 and num1 < num4:
    print(num1)
else:
    if num2 < num1 and num2 < num3 and num2 < num4:
        print(num2)
    else:
        if num3 < num1 and num3 < num2 and num3 < num4:
            print(num3)
        else:
            if num4 < num1 and num4 < num2 and num4 < num3:
                print(num4)