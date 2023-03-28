n1 = int (input('Número 1 = '))
n2 = int (input('Número 2 = '))
soma = n1+n2
subtração = n1-n2
multiplicação = n1*n2
divisão = n1/n2
potencia = n1**n2
divisão_i = n1//n2
resto = n1%n2
#Todas as operações acima juntamente com os valores, logo abaixo os resultados atráves do print
print ('1. {} \n2. {} \n2A multipicação é igual {} \nA divisão é igual {}\n'.format (soma, subtração, multiplicação, divisão),end ='')
print ('A potencia do n1 com o n2 é igual {} \nJá a divisão inteira é igual {} \nE por fim o resto da divisão inteira é {} :)'.format(potencia, divisão_i, resto))