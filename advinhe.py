import random

pontos = 0

while True:
    print('Pensei num numero de 1 a 5, consegue advinhar?')
    numero_pc = random.randint(1,5)
    numero_jogador = int(input('Seu numero: '))
    if numero_jogador == numero_pc: 
        pontos += 1
        print(f'Voce acertou! +1 ponto')
    else:
        print('Voce errou')
        break
print(f'Pontos finais {pontos}')
        

