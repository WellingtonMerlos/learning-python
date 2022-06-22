#Aqui eu faço a importação do modulo de randomização de numeros, que utilizarei no jogo de dados

from random import randint

#Apresentação do jogo
print('########################################################################\n'
      '________________________BEM VINDO AO ZOMBIE DICE________________________\n'
      '########################################################################')

#Pergunta a quantidade de jogadores, é feito o cadastro com restrição de no minimo 2 jogadores
numJogadores = 0
while True:
    numJogadores = int(input('Informe a quantidade de jogadores: '))
    if numJogadores < 2:
        print('AVISO: Você precisa de pelo menos 2 jogadores!')
    elif numJogadores >= 2:
        break
    else:
        print('INFORME UM NUMERO VALIDO!')

#Crio uma lista onde colocarei o nome dos jogadores
listaJogadores = []

#Jogador faz a inclusão dos nomes dos jogadores conforme a quantidade informada
#Os nomes são inclusos na lista
for i in range(numJogadores):
    nome = input(f'Informe o nome do {i + 1}º jogador: ')
    listaJogadores.append(nome)
print(f'Sejam bem vindos! {listaJogadores}')

#Dados disponiveis para jogar e suas possiveis faces e caixa com todos os dados inclusos

dadoVerde = ['C', 'P', 'C', 'T', 'P', 'C']
dadoAmarelo = ['T', 'P', 'C', 'T', 'P', 'C']
dadoVermelho = ['T', 'P', 'C', 'C', 'P', 'T']
caixaDados = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
              dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
              dadoVermelho, dadoVermelho, dadoVermelho]

print(' INICIANDO O JOGO...')
#defino o primeiro jogador da lista como o primeiro a jogar
jogadorAtual = 0
#lista de dados sorteados para armazenar os dados jogados
dadosSorteados = []

#placares de tiros, cerebros e passos iniciam zerados
tiros = 0
cerebros = 0
passos = 0

#aqui utilizo loop de repetição em que será quebrado quando o jogador escolher não jogar mais ou receber 3 tiros

while True:
    #mostra o jogador do turno atual
    print(f'Turno do jogador: {listaJogadores[jogadorAtual]}')
    input('Pressione ENTER para sortear 3 dados:')
    for i in range(3):
        #sorteado de 0 a 12, que são as posições na lista de dados
        numSorteado = randint(0, 12)
        #adiciono a face sorteada na lista de dados sorteados
        dadoSorteado = caixaDados[numSorteado]
        #informa ao jogador a cor do dado conforme a face
        if dadoSorteado == dadoVerde:
            corDado = 'VERDE'
        elif dadoSorteado == dadoAmarelo:
            corDado = 'AMARELO'
        else:
            corDado = 'VERMELHO'
        #mostra o dado sorteado
        print(f'{i +1}ª dado sorteado: {corDado}')

        #adiciona o dado na lista
        dadosSorteados.append(dadoSorteado)

    #Inicia lançamento dos dados sorteados
    input('Pressione ENTER para jogar os dados sorteados:')
    print(f'As faces sorteadas foram: {dadosSorteados}')

    #percorre cada um dos dados sorteados
    for dadoSorteado in dadosSorteados:

        #sorteia um numero aleatorio de 0 a 5, que são as faces do dado
        numFaceDado = randint(0, 5)

        #se for cerebro
        if dadoSorteado[numFaceDado] == 'C':
            print('CÉREBRO - Você comeu um cérebro')
            #contador de cerebros
            cerebros += 1

        #se for tiros
        elif dadoSorteado[numFaceDado] == 'T':
            print('TIRO - Você levou um tiro')
            tiros += 1

        #se for passos
        else:
            print('PASSOS - Uma vitima fugiu')
            passos += 1
    print(f'SCORE ATUAL: \nCÉREBROS: {cerebros} \nTIROS: {tiros}' )

    #pergunta se o jogador quer continuar a jogar ou salvar os pontos
    continuarTurno = input('DESEJA CONTINUAR JOGANDO? [S/N]: ').strip().upper()
    if continuarTurno == 'N':
        jogadorAtual += 1
        dadosSorteados = []
        tiros = 0
        cerebros = 0
        passos = 0
        if jogadorAtual == len(listaJogadores):
            print('Finalizando prototipo do jogo...')
            break
    else:
        print('iniciando mais uma rodada do turno atual...')
        dadosSorteados = []

#Obs: jogo ainda não concluido...


