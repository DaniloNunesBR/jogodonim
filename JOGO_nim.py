def computador_escolhe_jogada(n,m):
    m = m + 1
    multiplo = n % m
    count = 0
    if multiplo != 0:
        while multiplo != 0:
            n = n - 1
            count = count + 1
            multiplo = n % m
        return count
    else:
        m = m - 1
        return m

def usuario_escolhe_jogada(n,m):
    print("")
    retirar = int(input("Quantas peças vai tirar: "))
    if retirar > n:
        while retirar > n:
            print("Oops! Jogada inválida! Tente de novo.")
            print("")
            retirar = int(input("Quantas peças vai tirar: "))
    if retirar <= m and retirar > 0:
        return retirar
    else:
        while retirar > m or retirar <= 0:
            print("Oops! Jogada inválida! Tente de novo.")
            print("")
            retirar = int(input("Quantas peças vai tirar: "))
        return retirar
    
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    limit = m + 1
    multiplo = n % limit
    if multiplo != 0:
        print("")
        print("Computador começa!")
        print("")
    else:
        print("")
        print("Voce começa!")
        print("")
    while n != 0:
        multiplo = n % limit
        if multiplo != 0:
            tirar = computador_escolhe_jogada(n,m)
            n = n - tirar
            print("O Computador tirou",tirar,"peças")
            if n == 0:
                print("Não há mais peças no tabuleiro!" )
            else:
                print("Restam",n,"peças no tabuleiro.")
        else:
            tirar = usuario_escolhe_jogada(n,m)
            n = n - tirar
            print("")
            print("Você tirou",tirar,"peças")
            if n == 1:
                print("Resta apenas uma peça no tabuleiro! ")
                print("")
            else:
                print("Restam",n,"peças no tabuleiro.")
                print("")
    print("")
    print("Fim do jogo! O computador ganhou!")

def campeonato():
    print("")
    print("**** Rodada 1 ****")
    print("")
    partida()
    print("")
    print("**** Rodada 2 ****")
    print("")
    partida()
    print("")
    print("**** Rodada 3 ****")
    print("")
    partida()
    print("")
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você 0 X 3 Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha: ")
    print("")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato ")
    valor = int(input(""))
    if valor == 1 or valor == 2:
        if valor == 1:
            print("")
            print("Você escolheu uma partida! ")
            print("")
            partida()
        if valor == 2:
            print("")
            print("Você escolheu um campeonato! ")
            print("")
            campeonato()
    else:
        while valor != 1 and valor != 2:
            print("Oops! Opção inválida! Tente de novo.")
            valor = int(input(""))
        if valor == 1:
            print("")
            print("Você escolheu uma partida! ")
            print("")
            partida()
        if valor == 2:
            print("")
            print("Você escolheu um campeonato! ")
            print("")
            campeonato()

main()
