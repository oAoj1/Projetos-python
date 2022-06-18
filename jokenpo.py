import random

rodadas = 0
pontos = 0

print('JOKENPO Melhor de 3!')
while rodadas < 3:
    rodadas += 1
    jokenpo = random.randint(1,3)
    jogador = int(input('[1] Pedra\n[2] Papel\n[3] Tesoura\n=> '))

    if jogador == 1 and jokenpo == 3:
        pontos += 1
        print('Voce ganhou, \033[36mPedra > Tesoura\033[m')
    if jogador == 1 and jokenpo == 2:
        print('Voce perdeu, \033[31mPedra < Papel\033[m')
    if jogador == 2 and jokenpo == 1:
        pontos += 1
        print('Voce ganhou, \033[36mPapel > Pedra\033[m')
    if jogador == 2 and jokenpo == 3:
        print('Voce perdeu, \033[31mPapel < Tesoura\033[m')
    if jogador == 3 and jokenpo == 2:
        pontos += 1
        print('Voce ganhou, \033[36mTesoura > Papel\033[m')
    if jogador == 3 and jokenpo == 1:
        print('Voce perdeu, \033[31mTesoura < Pedra\033[m')
    if jogador == jokenpo:
        print('Empate')
print(f'Pontos finais: {pontos}')
