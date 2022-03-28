while True:
    nome = input('Palavra para soletrar: ')
    for letra in nome:
        print(f'{letra}')
    print()
    resp = input('Dsejas continuar? [S/N] ').upper()
    while (len(resp) != 1) or (resp not in 'SN'):
        print('Valor INVÁLIDO?')
        resp = input('Dsejas continuar? [S/N] ').upper()
    if resp == 'N':
        break