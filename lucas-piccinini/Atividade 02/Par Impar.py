#Jogo par ou impar, sozinho ou com amigo

from random import *

contadorP1 = 0
contadorP2 = 0
modo_jogo = int(input("Deseja jogar sozinho ou com um amigo? (sozinho = 0 / com amigo = 1)"))
if modo_jogo < 0 or modo_jogo > 1:
    print("Modo de jogo inválido")
else:
    rodadas = int(input("Quantas vitorias serâo necessarias para acabar o jogo? "))
    if rodadas < 1:
        print("Digite um numero valido de rodadas")
    else:
        while contadorP2 < rodadas and contadorP1 < rodadas:
            tipo = int(input("Deseja Par ou impar? (par = 0 / impar = 1)"))
            if tipo < 0 or tipo > 1:
                print("Apenas é aceito 0 e 1 como modo")
            else:
                jogador1 = int(input("Jogador 1, escolha um número:"))
                if modo_jogo == 0:
                    jogador2 = randint(1, 2)
                    resultado = (jogador1 + jogador2) % 2
                    statj2 = "Máquina"
                    if tipo == 0:
                        if resultado == 0:
                            print(f"Jogador 1 jogou {jogador1}, jogador 2 jogou {jogador2}, vencedor Jogador 1")
                            contadorP1 = contadorP1 + 1
                        else:
                            print(f"Jogador 1 jogou {jogador1}, Máquina jogou {jogador2}, vencedor Máquina")
                            contadorP2 = contadorP2 + 1
                    else:
                        if resultado == 0:
                            print(f"Jogador 1 jogou {jogador1}, Máquina jogou {jogador2}, vencedor Máquina")
                            contadorP2 = contadorP2 +1
                        else:
                            print(f"Jogador 1 jogou {jogador1}, jogador 2 jogou {jogador2}, vencedor Jogador 1")
                            contadorP1 = contadorP1 + 1
                else:
                    jogador2 = int(input("Jogador 2, escolha um número:"))
                    resultado = (jogador1 + jogador2) % 2
                    statj2 = "Jogador 2"
                    if tipo == 0:
                        if resultado == 0:
                            print(f"Jogador 1 jogou {jogador1}, jogador 2 jogou {jogador2}, vencedor Jogador 1")
                            contadorP1 = contadorP1 + 1
                        else:
                            print(f"Jogador 1 jogou {jogador1}, jogador 2 jogou {jogador2}, vencedor Jogador 2")
                            contadorP2 = contadorP2 + 1
                    else:
                        if resultado == 0:
                            print(f"Jogador 1 jogou {jogador1}, jogador 2 jogou {jogador2}, vencedor Jogador 2")
                            contadorP2 = contadorP2 + 1
                        else:
                            print(f"Jogador 1 jogou {jogador1}, jogador 2 jogou {jogador2}, vencedor Jogador 1")
                            contadorP1 = contadorP1 + 1

        print(f"placar final: jogador 1: {contadorP1} - {statj2}: {contadorP2}")
        if jogador1 > jogador2:
            print("Vencedor jogador 1")
        else:
            print(f"Vencedor: {statj2}")
