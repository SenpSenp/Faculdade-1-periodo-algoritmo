#. Faça um algoritmo que receba o valor do salário de uma pessoa e o valor de um
#financiamento pretendido. Caso o financiamento seja menor ou igual a 5 vezes o
#salário da pessoa, o algoritmo deverá escrever "Financiamento Concedido"; senão,
#ele deverá escrever "Financiamento Negado".

salario = float(input("Qual seu salário? "))
financiamento = float(input("Qual o valor do financiamento? "))
salario5 = salario * 5

if financiamento <= salario5:
    print("financiamento concedido")
else:
    print("Financiamento negado")