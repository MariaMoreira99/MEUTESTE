from random import randint
maquina = randint(1, 100)
print('Pensei em um número entre 1 e 100.')
print('Vamos tentar adivinhar? ')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual o numero? '))
    tentativas += 1
    if jogador == numero:
        acertou = True
    else:
        if jogador < numero:
            print('O número é maior.')
        elif jogador > numero:
            print('O número é menor.')
print('Você acertou o número com {} tentativas!' .format(tentativas))

