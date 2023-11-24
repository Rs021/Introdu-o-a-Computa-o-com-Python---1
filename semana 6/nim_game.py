
def computador_escolhe_jogada(n,m):


    jogada = 1
    while jogada <= 1:
        if (n - jogada) % (m + 1) != 0:
            print(f"O computador tirou {jogada} peças.")
            return jogada
        else:
            jogada += 1

    print(f"O computador tirou {jogada} peças.")
    return jogada


def usuario_escolhe_jogada(n,m):
    m_retirar = int(input("Quantas peças você vai tirar?")) 
    while m_retirar > n or m_retirar < 1:
            print("Oops! Jogada inválida! Tente de novo.")
            m_retirar = int(input("Quantas peças você vai tirar?")) 

    print(f"Voce tirou {m_retirar} peças.")
    return n - m_retirar

def partida():
        print("**** Rodada ****")
        
        n = int(input("Quantas peças?"))
        m = int(input("Limite de peças por jogada?"))

        a = False

        if n % (m + 1) == 0:
            a = True
        
        
        print("Computador começa!")
        while n > 0:

            if a:
                n = usuario_escolhe_jogada(n,m)
            
            else:
                n = computador_escolhe_jogada(n,m)
                
            print(f"Agora restam {n} peças no tabuleiro.")

            a = not a
            
   

        if a:
            print("Você ganhou!")
            return 1
        else:
            print("O computador ganhou!")
            return 2      



def campeonato():
    placar_usuario = 0
    placar_computador = 0

    for _ in range(3):
        print(f"**** Rodada {_ + 1} ****")
        resultado = partida()

        if resultado % 2 == 0:
            placar_computador += 1
        else:
            placar_usuario += 1

    print("**** Final do campeonato! ****")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = int(input())


    if escolha == 1:
            
        print("Voce escolheu um Partida!")
        partida()


    elif escolha == 2:
            
        print("Voce escolheu um campeonato!")
        campeonato()
    else:
        print("Digite um numero partida valido")

   

if __name__ == "__main__":
    main()
    #computador_escolhe_jogada(15,5)