#Desenvolva um algoritmo para que, dados dois valores inteiros entre 1 e 10 lidos,
#calcule e imprima: a média dos números caso a soma deles for menor que 8, seu
#produto caso a soma seja igual a 8 ou a divisão do maior pelo menor caso a soma
#dos valores for maior que 8.

num1 = int(input("Digite um numero entre 1 e 10: "))
num2 = int(input("Digite outro numero entre 1 e 10: "))
soma = num1+num2

if soma < 8:
    print(f"{(num1 + num2) / 2:.0f}")
else:
    if soma == 8:
        print(f"{num1 * num2:.0f}")
    else:
        if soma > 8:
            if num1 > num2:
                print(f"{num1 / num2:.0f}")
            if num2 > num1:
                print(f"{num2 / num1:.0f}")