q = int(input("quantas conversões = "))

for md in range (q):
    reais = float(input('reais = R$'))
    dolar =reais/5.07
    print (f'dolar = U${dolar:.2f}')
