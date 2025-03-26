frase = 'deivid'

i = 0 
mais_repetida = 0 
letra_apareceu =''

while i < len(frase):
    
    letra_atual = frase[i]
    mais_repetida_atual = frase.count(letra_atual)
    
    if letra_atual == '':
        i+=1
        continue
    if mais_repetida<mais_repetida_atual:
        mais_repetida = mais_repetida_atual
        letra_apareceu = letra_atual

    i+=1
print('A letra mais repetida foi '
f'*{letra_apareceu}* que apareceu {mais_repetida} vezes')
...