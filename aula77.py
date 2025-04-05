import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
erros = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = (pergunta['Opções'])

    for i,opcao in enumerate(opcoes):

        print(f'{i})', opcao)

        print()
    



    escolha = input('Digite a opção: ')

    os.system('cls')

    acertou = False
    escolha_int = None
    qnt_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
        
    if escolha_int is not None:
        if escolha_int >=0 and escolha_int <qnt_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    
    if acertou:
        acertos +=1
    else:
        erros+=1

print(f'Você acertou {acertos} questões')
if erros > 0:
    print(f'Você errou {erros} questões')

    

        

    