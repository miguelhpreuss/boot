#Miguel Hellmann Preuss
#insta: miguelhpreuss
#Descrição: Sorteador de numeros de mega-sena

from random import sample, randint

#configurações
quantidade_de_numeros = 6
quantidade_de_jogos = 2

for jogo in range(0, quantidade_de_jogos):
    lista = []
    for i in range(0, quantidade_de_numeros):
        continuar = False
        while not continuar:
            numero_random = randint(1, 60)
            if (len(lista) == 0):
                continuar = True
            for n in range(0, len(lista)):
                if numero_random == lista[n]:
                    break
                if lista[n] == lista[-1]:
                    continuar = True
                
        lista.append(numero_random)
    lista.sort()
    print("Jogo nº {}: ".format(jogo + 1) + str(lista))
