
def computador_escolhe_jogada(n,m):


    peca = 1

    while peca != m:

        if (n - peca) % (m + 1) == 0:
            return peca
            
        else:
            peca += 1

    return peca


def usuario_escolhe_jogada(n,m):

    valid = False


    while not valid:   
        m_retirar = int(input("Quantas peças você vai tirar?")) 
        if m_retirar > m or m_retirar < 1:  
            print("Oops! Jogada inválida! Tente de novo.")

        else:
            valid = True

    return m_retirar
    
    

def partida():
    n = int(input('Quantas peças? '))

    m = int(input('Limite de peças por jogada? '))

    pc = False

    if n % (m+1) == 0:
        print()
        print('Voce começa!')

    else:
        print()
        print('Computador começa!')
        pc = True

    while n > 0:
        if pc:
            peca_pc = computador_escolhe_jogada(n, m)
            n = n - peca_pc
            if peca_pc == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', peca_pc, 'peças')

            pc = False
        else:
            peca_jg = usuario_escolhe_jogada(n, m)
            n = n - peca_jg
            if peca_jg == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', peca_jg, 'peças')
            pc = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')


def campeonato():
    
    rodada = 1

    while rodada <= 3:
        print('**** Rodada', rodada, '****')    
        partida()
        rodada += 1

    print("**** Final do campeonato! ****")
    print('Placar: Você 0 X 3 Computador')


print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

escolha = int(input())


if escolha == 1:
            
        print("Voce escolheu um Partida!")
        partida()

else:
            
    print("Voce escolheu um campe   onato!")
    campeonato()
    
   

