#pedra papel tesoura, 1 jogada, 2 jogadores

print("Pedra, papel, tesoura, digite sua jogada seguindo o padrâo: 1 = Pedra, 2 = Papel, 3 = Tesoura")
jogador1 = int(input("jogador1, digite sua jogada: "))
jogador2 = int(input("jogador2, digite sua jogada: "))

if jogador1 == 1 and jogador2 == 1:
    print("Jogador 1 e Jogador 2 jogaram Pedra, Empate!")
else:
    if jogador1 == 2 and jogador2 == 2:
        print("Jogador 1 e Jogador 2 jogaram Papel, Empate!")
    else:
        if jogador1 == 3 and jogador2 == 3:
            print("Jogador 1 e Jogador 2 jogaram Tesoura, Empate!")
        else:
            if jogador1 == 1 and jogador2 == 3:
                print("Jogador 1 jogou Pedra, Jogador 2 jogou Tesoura, Jogador 1 Venceu")
            else:
                if jogador1 == 2 and jogador2 == 1:
                    print("Jogador 1 jogou Papel, Jogador 2 jogou Pedra, Jogador 1 Venceu!")
                else:
                    if jogador1 == 3 and jogador2 == 2:
                        print("Jogador 1 jogou Tesoura, Jogador 2 jogou Papel, Jogador 1 Venceu!")
                    else:
                        if jogador1 == 1 and jogador2 == 2:
                            print("Jogador 1 jogou Pedra, jogador 2 jogou Papel, jogador 2 venceu!")
                        else:
                            if jogador1 == 2 and jogador2 == 3:
                                print("Jogador 1 jogou Papel, Jogador 2 jogou Tesoura, Jogador 2 Venceu!")
                            else:
                                if jogador1 == 3 and jogador2 == 1:
                                    print("Jogador 1 jogou Tesoura, Jogador 2 jogou Pedra, Jogador 2 Venceu!")
                                else:
                                    print("Jogada inválida, tente novamente")
