from random import randint
v = 0
while True:
    usuario = int(input('Digite um número de 0 a 10:'))
    computador = randint(0, 10)
    total = usuario + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você escolhe par ou ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {usuario} e o computador {computador}. Total de {total} ', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'FIM DE JOGO! Você venceu {v} vezes.')
