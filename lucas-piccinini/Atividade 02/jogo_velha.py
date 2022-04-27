#pi = posição inicial
pi1 = "1"
pi2 = "2"
pi3 = "3"
pi4 = "4"
pi5 = "5"
pi6 = "6"
pi7 = "7"
pi8 = "8"
pi9 = "9"

vencedor = False
jogada_valida = False


while jogada_valida == False:
    print(f"{pi1}, {pi2}, {pi3}\n{pi4}, {pi5}, {pi6}\n{pi7}, {pi8}, {pi9}")

    jogada1 = int(input("Jogador 1, digite a posição que deseja jogar sua peça: "))
    if jogada1 < 1 or jogada1 > 9:
        print("Erro")
        jogada_valida = True
    else:
        while pi1 == "O" and jogada1 == 1 or pi2 == "O" and jogada1 == 2 or pi3 == "O" and jogada1 == 3 or pi4 == "O" and jogada1 == 4 or pi5 == "O" and jogada1 == 5 or pi6 == "O" and jogada1 == 6 or pi7 == "O" and jogada1 == 7 or pi8 == "O" and jogada1 == 8 or pi9 == "O" and jogada1 == 9 or pi1 == "X" and jogada1 == 1 or pi2 == "X" and jogada1 == 2 or pi3 == "X" and jogada1 == 3 or pi4 == "X" and jogada1 == 4 or pi5 == "X" and jogada1 == 5 or pi6 == "X" and jogada1 == 6 or pi7 == "X" and jogada1 == 7 or pi8 == "X" and jogada1 == 8 or pi9 == "X" and jogada1 == 9:
            print("Jogada inválida!!")
            jogada1 = int(input("Jogador 1, jogue novamente: "))
        if jogada1 == 1:
            pi1 = "O"
        else:
            if jogada1 == 2:
                pi2 = "O"
            else:
                if jogada1 == 3:
                    pi3 = "O"
                else:
                    if jogada1 == 4:
                        pi4 = "O"
                    else:
                        if jogada1 == 5:
                            pi5 = "O"
                        else:
                            if jogada1 == 6:
                                pi6 = "O"
                            else:
                                if jogada1 == 7:
                                    pi7 = "O"
                                else:
                                    if jogada1 == 8:
                                        pi8 = "O"
                                    else:
                                        if jogada1 == 9:
                                            pi9 = "O"
        if pi1 == pi2 == pi3 == "O" or pi4 == pi5 == pi6 == "O" or pi7 == pi8 == pi9 == "O" or pi1 == pi4 == pi7 == "O" or pi2 == pi5 == pi8 == "O" or pi3 == pi6 == pi9 == "O" or pi1 == pi5 == pi9 == "O" or pi3 == pi5 == pi7 == "O":
            vencedor = "Vencedor: Jogador 1"
            jogada_valida = True
        else:
            if pi1 != "1" and pi2 != "2" and pi3 != "3" and pi4 != "4" and pi5 != "5" and pi6 != "6" and pi7 != "7" and pi8 != "8" and pi9 != "9":
                vencedor = "Empate!!"
                jogada_valida = True
            else:
                print(f"{pi1}, {pi2}, {pi3}\n{pi4}, {pi5}, {pi6}\n{pi7}, {pi8}, {pi9}")
                jogada2 = int(input("Jogador 2, digite a posição que deseja jogar sua peça: "))

                if jogada2 < 1 or jogada2 > 9:
                    print("Erro")
                    jogada_valida = True
                else:
                    while pi1 == "O" and jogada2 == 1 or pi2 == "O" and jogada2 == 2 or pi3 == "O" and jogada2 == 3 or pi4 == "O" and jogada2 == 4 or pi5 == "O" and jogada2 == 5 or pi6 == "O" and jogada2 == 6 or pi7 == "O" and jogada2 == 7 or pi8 == "O" and jogada2 == 8 or pi9 == "O" and jogada2 == 9 or pi1 == "X" and jogada2 == 1 or pi2 == "X" and jogada2 == 2 or pi3 == "X" and jogada2 == 3 or pi4 == "X" and jogada2 == 4 or pi5 == "X" and jogada2 == 5 or pi6 == "X" and jogada2 == 6 or pi7 == "X" and jogada2 == 7 or pi8 == "X" and jogada2 == 8 or pi9 == "X" and jogada2 == 9:
                        print("Jogada inválida!!")
                        jogada2 = int(input("Jogador 2, jogue novamente: "))
                    else:
                        if jogada2 == 1:
                            pi1 = "X"
                        else:
                            if jogada2 == 2:
                                pi2 = "X"
                            else:
                                if jogada2 == 3:
                                    pi3 = "X"
                                else:
                                    if jogada2 == 4:
                                        pi4 = "X"
                                    else:
                                        if jogada2 == 5:
                                            pi5 = "X"
                                        else:
                                            if jogada2 == 6:
                                                pi6 = "X"
                                            else:
                                                if jogada2 == 7:
                                                    pi7 = "X"
                                                else:
                                                    if jogada2 == 8:
                                                        pi8 = "X"
                                                    else:
                                                        if jogada2 == 9:
                                                            pi9 = "X"

                if pi1 == pi2 == pi3 == "X" or pi4 == pi5 == pi6 == "X" or pi7 == pi8 == pi9 == "X" or pi1 == pi4 == pi7 == "X" or pi2 == pi5 == pi8 == "X" or pi3 == pi6 == pi9 == "X" or pi1 == pi5 == pi9 == "X" or pi3 == pi5 == pi7 == "X":
                    vencedor = "Vencedor: Jogador 2"
                    jogada_valida = True





#fim de jogo
print("---------------------")
if vencedor == True:
    print(f"\n\n{pi1}, {pi2}, {pi3}\n{pi4}, {pi5}, {pi6}\n{pi7}, {pi8}, {pi9}")
    print(f"Resultado final: {vencedor}")