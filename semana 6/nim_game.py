n_global = 0
m_global = 0
numero_rodada = 1


def computador_escolhe_jogada():
    m_retirar = int(input("Quantas peças você vai tirar?"))

    print(f"Voce tirou {m_retirar} peças.")
    print(f"Agora resta apenas {m_global} peça no tabuleiro.")


def usuario_escolhe_jogada():
    m_retirar = int(input("Quantas peças você vai tirar?"))

    print(f"Voce tirou {m_retirar} peças.")
    print(f"Agora resta apenas {m_global} peça no tabuleiro.")


def partida():
    print("**** Rodada 1 ****")
    n_global = int(input("Quantas peças?"))
    m_global = int(input("Limite de peças por jogada?"))

    if n_global % m_global + 1 == 0:
        usuario_escolhe_jogada()
        print("Jogador começa")
    else:
        print("Computador começa!")
        computador_escolhe_jogada()


def campeonato():
    partida()
    partida()
    partida()
    pass


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    opt = int(input())

    if opt == 1:
        partida()


    elif opt == 2:
        campeonato()

    else:
        print("Digite um numero partida valido")


if __name__ == "__main__":
    main()