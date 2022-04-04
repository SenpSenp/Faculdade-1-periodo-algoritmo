#pedra papel tesoura, 1 jogador vs máquina, 1 jogada

print("Pedra, papel, tesoura, digite sua jogada seguindo o padrâo: 1 = Pedra, 2 = Papel, 3 = Tesoura")
jogador1 = int(input("jogador1, digite sua jogada: "))

from random import *
jogada = (randint(0, 2))

if jogador1 == 1 and jogada == 0:
    print("Máquina jogou Pedra, empate")
else:
    if jogador1 == 2 and jogada == 1:
        print("Máquina jogou Papel, empate")
    else:
        if jogador1 == 3 and jogada == 2:
            print("Máquina jogou Tesoura, empate")
        else:
            if jogador1 == 1 and jogada == 2:
                print("Máquina jogou Tesoura, Você venceu!")
            else:
                if jogador1 == 2 and jogada == 0:
                    print("Máquina jogou Pedra, Você venceu!")
                else:
                    if jogador1 == 3 and jogada == 1:
                        print("Máquina jogou Papel, Você venceu!")
                    else:
                        if jogador1 == 1 and jogada == 1:
                            print("Máquina jogou Papel, Você perdeu :c")
                        else:
                            if jogador1 == 2 and jogada == 2:
                                print("Máquina jogou Tesoura, Você perdeu :c")
                            else:
                                if jogador1 == 3 and jogada == 0:
                                    print("Máquina jogou Pedra, Você perdeu :c")
                                else:
                                    print("Jogada inválida, tente novamente")
