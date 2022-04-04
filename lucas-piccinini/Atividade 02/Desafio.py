#pedra papel tesoura, 1 jogada, 2 jogadores, jogadas por nuúmeros

print("Pedra, papel, tesoura, digite sua jogada seguindo o padrâo: 1 = Pedra, 2 = Papel, 3 = Tesoura")
jogador1 = int(input("jogador1, digite sua jogada: "))
jogador2 = int(input("jogador2, digite sua jogada: "))

if jogador1 == 1 and jogador2 == 1 or jogador1 == 2 and jogador2 == 2 or jogador1 == 3 and jogador2 == 3:
    print("Empate")
else:
    if jogador1 == 1 and jogador2 == 3 or jogador1 == 3 and jogador2 == 2 or jogador1 == 2 and jogador2 == 1:
        print("Jogador 1 Venceu")
    else:
        if jogador2 == 1 and jogador1 == 3 or jogador2 == 3 and jogador1 == 2 or jogador2 == 2 and jogador1 == 1:
            print("Jogador 2 Venceu")
        else:
            print("Jogada inválida, tentar novamente.")
