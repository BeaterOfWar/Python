m = float (input('Tamanho em Metros = '))
mm = int (m*1000)
cm = int(m*100)
dm = int (m*10)
dam = m/10
hm = m/100
km = m/1000
print (f'Em Milimetros = {mm}\nEm Centimetros = {cm}\nEm Decimetro = {dm} ',end ='')
print (f'\nEm Decâmetro = {dam:.1f} \nEm Hectometros = {hm:.1f} \nEm Kilômetros = {km}')
