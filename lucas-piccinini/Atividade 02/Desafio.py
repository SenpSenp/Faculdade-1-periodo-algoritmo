#pedra papel tesoura, 1 jogada, 2 jogadores

print("Pedra, papel, tesoura, digite sua jogada com a primeira letra maiúscula")
jogador1 = input("jogador1, digite sua jogada: ")
jogador2 = input("jogador2, digite sua jogada: ")

if jogador1 == "Pedra" and jogador2 == "Pedra" or jogador1 == "Papel" and jogador2 == "Papel" or jogador1 == "Tesoura" and jogador2 == "Tesoura":
    print("Empate")
else:
    if jogador1 == "Pedra" and jogador2 =="Tesoura" or jogador1 == "Tesoura" and jogador2 == "Papel" or jogador1 == "Papel" and jogador2 == "Pedra":
        print("Jogador 1 Venceu")
    else:
        if jogador2 == "Pedra" and jogador1 == "Tesoura" or jogador2 == "Tesoura" and jogador1 == "Papel" or jogador2 == "Papel" and jogador1 == "Pedra":
            print("Jogador 2 Venceu")
        else:
            print("Jogada inválida, tentar novamente.")