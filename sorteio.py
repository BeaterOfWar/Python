import random
n = int(input('Quantidade de nomes = '))
ns = int(input('Numero de sorteios = '))
nomes= []
for repeticao in range (n):
    while nome:
        nome = input('Insira um nome = ')
        nomes.append(nome)
    if ns == 1:
        sorteio = random.choice(nomes)
    else:
        sorteio = random.choices(nomes)

print (f'Vencedor(es) do sorteio{sorteio}')