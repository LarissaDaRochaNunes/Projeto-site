while conf == 'nN'
    n1= str(input('Nome completo: '))
    n2= int(input('Idade: '))
    n3= str(input('Sexo [M/F]'))
    if n3 != 'MmFf':
        n3= str(input('Sexo [M/F]'))
    print('INFORMAÇÕES PARA CADASTRO:')
    print(f'Nome:{n1}'
          f'Idade: {n2}'
          f'Sexo: {n3}')
    conf= str(input('Os dados estão corretos? [S/N]'))
    print('CADASTRO REALIZADO COM SUCESSO')