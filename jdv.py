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

    posicao = int(input(f"jogador {jogador}, escolha uma posição de 1 à 9:")) - 1
    
    if tabuleiro[posicao] == " ":
        tabuleiro[posicao] = jogador
    else:
        print("essa posição já está ocupada :(")
        continue
    
    if verificacao_vitorias():
        exibir_tabuleiro()
        print(f"jogador {jogador} venceu:)")
        break
    if verificacao_empate():
        exibir_tabuleiro()
        print("empate:/")
    if jogador == "x":
        jogador == "o"
    else:
        jogador = "x"