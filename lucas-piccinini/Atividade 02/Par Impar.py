#Jogo par ou impar, sozinho ou com amigo

from random import *

modo_jogo = int(input("Deseja jogar sozinho ou com um amigo? (sozinho = 0 / com amigo = 1)"))
if modo_jogo < 0 or modo_jogo > 1:
    print("Modo de jogo inválido")
else:
    tipo = int(input("Deseja Par ou impar? (par = 0 / impar = 1)"))
    if tipo < 0 or tipo > 1:
        print("Apenas é aceito 0 e 1 como modo")
    else:
        jogador1 = int(input("Jogador 1, escolha um número:"))
        if modo_jogo == 0:
            jogador2 = (randint(0, 1))
            resultado = (jogador1 + jogador2) % 2
            if tipo == 0:
                if resultado == 0:
                    vencedor = "Jogador 1"
                else:
                    vencedor = "Máquina"
            else:
                if resultado == 0:
                    vencedor = "Máquina"
                else:
                    vencedor = "Jogador 1"
        else:
            jogador2 = int(input("Jogador 2, escolha um número:"))
            resultado = (jogador1 + jogador2) / 2
            if tipo == 0:
                if resultado == 0:
                    vencedor = "Jogador 1"
                else:
                    vencedor = "Jogador 2"
            else:
                if resultado == 0:
                    vencedor = "Jogador 2"
                else:
                    vencedor = "Jogador 1"

        print(f"{jogador1} + {jogador2} = {jogador1+jogador2:.0f}")
        print(f"Vencedor: {vencedor}")
