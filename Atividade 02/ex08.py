#Faça a leitura do ano atual e do ano de nascimento de uma pessoa e exibir sua idade.
#A seguir, informe se a pessoa é bebê (0 a 3 anos), criança (4 a 10 anos), adolescente
#(11 a 18 anos), adulta (19 a 50 anos) ou idosa (51 anos em diante).

ano_atual = int(input("Qual ano estamos? "))
ano_nascimento = int(input("Em qual ano você nasceu? "))
idade = ano_atual-ano_nascimento

if idade < 4:
    print("Você é um bebê")
else:
    if idade < 10:
        print("Você é uma criança")
    else:
        if idade < 18:
            print("Você é um adolescente")
        else:
            if idade < 50:
                print("Você é um adulto")
            else:
                print("Você é um idoso")