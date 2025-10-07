def computador_escolhe_jogada(n,m):
    for i in range (1 , m + 1):
        if (n - i) % (m + 1) == 0:
            return i
        return min(n,m)


def usuario_escolhe_jogada(n,m):
    while True:
        try:
            jogada = int(input('Quantas peças você vai tirar? '))
            if 1 <= jogada <= m and jogada <= n:
                return jogada
            else:
                print('Oops! Jogada inválida. Tente de novo.')
        except ValueError:
            print('Por favor, insira um número válido.')


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    if n % (m+1) == 0:
        print('Você começa!')
        vez_do_usuario = True
    else:
        print('Computador começa')
        vez_do_usuario = False
    while n > 0:
        if vez_do_usuario:
            jogada = usuario_escolhe_jogada(n,m)
            print(f'Você tirou {jogada} peça(s).')
        else:
            jogada = computador_escolhe_jogada(n,m)
            print(f'O computador tirou {jogada} peça(s). ')
            n -= jogada
            if n == 0:
                if vez_do_usuario:
                    print('Você ganhou!')
                else:
                    print('O computador ganhou!')
                break
            else:
                print(f'Agora restam {n} peça(s) no tabuleiro. ')
            vez_do_usuario = not vez_do_usuario


def campeonato():
    usuario = 0
    computador = 0
    for i in range(1,4):
        print(f'\n*** Rodada {i} ***\n')
        if partida():
            usuario += 1
        else:
            computador +=1
    print('\n*** Final do campeonato! ***')
    print(f'Placar: você {usuario} X {computador} computador ')

print('BEM-VINDO AO JOGO DO NIM!, Escolha:')
print('1 - Para jogar uma partida isolada')
print('2 - Para jogar um campeonato')
opcao = int(input('Opção: '))
if opcao == 1:
    print('\nVocê escolheu uma partida isolada!')
    partida()
elif opcao == 2:
    print('\nVocê escolheu um campeonato!')
    campeonato()
else:
    print('Opção inválida!')
