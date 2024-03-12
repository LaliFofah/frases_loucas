from random import choice

adjetivo = ''
nomeComum1 = ''
nomeComum2 = ''
nomeComum3 = ''
nomeComum4 = ''
nomeComum5 = ''
nomeColetivo = ''
nomeProprio = ''
verbo1 = ''
verbo2 = ''
pronome1 = ''
pronome2 = ''
adverbio = ''

frase = [f'{pronome1} {verbo1} {adverbio} como {pronome2} {nomeComum1}', f'se {pronome1} {verbo1} {nomeComum1} {pronome2} {verbo2} {nomeComum2}', f'Sabes qual é a coisa que mais gosto em ti, {nomeProprio}? É o facto de seres {adverbio} {adjetivo}', f'{pronome1} {nomeComum1} dançou salsa com {nomeComum2} enquanto usava um {nomeComum3} {adjetivo}', f'Numa reviravolta bizarra, todos os {nomeComum1} do mundo formaram uma aliança para exigir {nomeComum2} 24 horas por dia, 7 dias por semana, {nomeComum3} com sabor a {nomeColetivo} e sessões obrigatórias de {nomeComum4} com humanos, declarando-se os senhores supremos da {nomeComum5}.']
numFrases = [0, 1, 2, 3, 4]
randomNum = choice(numFrases)
if (randomNum == 0):    
    pronome1 = input('Insira um pronome: ')
    verbo1 = input('Insira um verbo: ')
    adverbio = input('Insira um adverbio de modo: ')
    pronome2 = input('Insira um pronome indefinido: ')
    nomeComum1 = input('Insira um nome comum: ')
    frase[0] = f'{pronome1} {verbo1} {adverbio} como {pronome2} {nomeComum1}'
    print(frase[0])
elif (randomNum == 1):
    pronome1 = input('Insira um pronome: ')
    verbo1 = input('Insira um verbo: ')
    nomeComum1 = input('Insira um nome comum: ')
    pronome2 = input('Insira um pronome: ')
    verbo2 = input('Insira um verbo: ')
    nomeComum2 = input('Insira um nome comum: ')
    frase[1] = f'{pronome1} {verbo1} {adverbio} como {pronome2} {nomeComum1}'
    print(frase[1])
elif (randomNum == 2):
    nomeProprio = input('Insira um nome próprio: ')
    adverbio = input('Insira um adverbio: ')
    adjetivo = input('Insira um adjetivo: ')
    frase[2] = f'Sabes qual é a coisa que mais gosto em ti, {nomeProprio}? É o facto de seres {adverbio} {adjetivo}'
    print(frase[2])
elif (randomNum == 3):
    pronome1 = input('Insira um pronome indefinido')
    nomeComum1 = input('Insira um nome comum: ')
    nomeComum2 = input('Insira um nome comum: ')
    nomeComum3 = input('Insira um nome comum: ')
    adjetivo = input('Insira um nome adjetivo: ')
    frase[3] = f'O {nomeComum1} dançou salsa com {nomeComum2} enquanto usava um {nomeComum3} {adjetivo}'
    print(frase[3])
elif (randomNum == 4):
    nomeComum1 = input('Insira um nome comum: ')
    nomeComum2 = input('Insira um nome comum: ')
    nomeComum3 = input('Insira um nome comum: ')
    nomeColetivo = input('Insira um nome comum coletivo: ')
    nomeComum4 = input('Insira um nome comum: ')
    nomeComum5 = input('Insira um nome comum: ')
    frase[4] = f'Numa reviravolta bizarra, todos os {nomeComum1} do mundo formaram uma aliança para exigir {nomeComum2} 24 horas por dia, 7 dias por semana, {nomeComum3} com sabor a {nomeColetivo} e sessões obrigatórias de {nomeComum4} com humanos, declarando-se os senhores supremos da {nomeComum5}.'
    print(frase[4])