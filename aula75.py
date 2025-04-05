# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicar(multiplicador):
    def calculo(numero):
        return multiplicador*numero

    return calculo

duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadruplicar = multiplicar(4)
print(duplicar(2))