import random
p1 = input('Digite um nome = ')
p2 = input('Digite um nome = ')
p3 = input('Digite um nome = ')
p4 = input('Digite um nome = ')
lista = [p1,p2,p3,p4]
sorteio = random.choice(lista)
print (f'A pessoa escolhida foi = {sorteio}')
