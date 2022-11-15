def testa_par(x):
    if x % 2 == 0:
        print(x, 'é um número par')
    else:
        print(x, 'é um número ímpar')


def testa_primo(valor):
    teste = 0
    for individuo in range(2, valor):
        if valor % individuo == 0:
            teste = teste+1
    if teste != 0:
        print(valor, 'não é primo')
    else:
        print(valor, 'é primo')


def testa_perfeito(gretagarbo):
    verifica = 1
    for qualquerum in range(1, gretagarbo):
        if gretagarbo % qualquerum == 0:
            verifica = verifica+qualquerum
    if verifica == gretagarbo:
        print(gretagarbo, 'é perfeito')
    else:
        print(gretagarbo, 'não é perfeito')


def procura_divisores(n):
    lista_de_divisores = []
    for i in range(1, n):
        if n % i == 0:
            lista_de_divisores.append(i)
    if len(lista_de_divisores) == 0:
        print(n, 'Não tem divisores')
    else:
        print('Divisores de', n, ':')
        for i in lista_de_divisores:
            print(i,)


def soma_algarismos(n):
    n = str(n)
    while len(n) > 1:
        m = 0
        for i in n:
            m = m+int(i)
            n = str(m)
    print(n)


n = int(input('Digite o número a ser analisado: '))
testa_par(n)
testa_primo(n)
testa_perfeito(n)
procura_divisores(n)
soma_algarismos(n)
