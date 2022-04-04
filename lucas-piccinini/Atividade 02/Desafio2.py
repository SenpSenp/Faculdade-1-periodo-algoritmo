#pedra papel tesoura, 1 jogada, 2 jogadores

print("Pedra, papel, tesoura, digite sua jogada seguindo o padrâo: 1 = Pedra, 2 = Papel, 3 = Tesoura")
jogador1 = int(input("jogador1, digite sua jogada: "))

from random import *
jogada = (randint(0, 2))

if jogador1 == 1 and jogada == 0 or jogador1 == 2 and jogada == 1 or jogador1 == 3 and jogada == 2:
    print(f"Máquina jogou {jogada+1}")
    print("Empate")
else:
    if jogador1 == 1 and jogada == 2 or jogador1 == 3 and jogada == 1 or jogador1 == 2 and jogada == 0:
        print(f"Máquina jogou {jogada + 1}")
        print("Jogador 1 Venceu")
    else:
        if jogada == 0 and jogador1 == 3 or jogada == 2 and jogador1 == 2 or jogada == 1 and jogador1 == 1:
            print(f"Máquina jogou {jogada + 1}")
            print("Jogador 2 Venceu")
        else:
            print("Jogada inválida, tentar novamente.")