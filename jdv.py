import random


tabuleiro = [" ", " ", " ", 
             " ", " ", " ", 
             " ", " ", " "]

jogador = "x"

def exibir_tabuleiro():
    print()
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("--+---+--")
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("--+---+--")
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print()

def verificacao_vitorias():
    combinacoes = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for combinacao in combinacoes:
        a, b, c = combinacao
        
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] != " ":
            return True

    return False

def verificacao_empate():
    return " " not in tabuleiro

while True: 
    exibir_tabuleiro()

    if jogador == "x":
        posicao = int(input(f"jogador {jogador}, escolha uma posição de 1 à 9: ")) - 1

        if posicao < 0 or posicao > 8:
            print("Posição inválida.")
            continue

        if tabuleiro[posicao] != " ":
            print("essa posição já está ocupada :(")
            continue

        tabuleiro[posicao] = jogador
    else:
        print("computador jogando, aguarde um momento...")
        posicoes_disponiveis = [i for i, v in enumerate(tabuleiro) if v == " "]
        if posicoes_disponiveis:
            posicao = random.choice(posicoes_disponiveis)
            tabuleiro[posicao] = jogador

    if verificacao_vitorias():
        exibir_tabuleiro()

        if jogador == "x":
            print("Você venceu :)")
        else:
            print("O computador venceu :(")

        break

    if verificacao_empate():
        exibir_tabuleiro()
        print("Empate :/")
        break

    jogador = "o" if jogador == "x" else "x"
