#Fça a leitura do salário atual e do tempo de serviço de um funcionário. A seguir,
#calcule o seu salário reajustado. Funcionários com até 1 ano de empresa, receberão
#aumento de 10%. Funcionários com mais de um ano de tempo de serviço, receberão
#aumento de 20%.

salario = float(input("Qual seu salário atual? "))
tempo = int(input("Quantos anos está na empresa? "))
salario10 = salario * 1.10
salario20 = salario * 1.20

if tempo <= 1:
    print(f"Seu salário vai ser de {salario10:.2f}")
else:
    print(f"Seu salário vai ser de {salario20:.2f}")