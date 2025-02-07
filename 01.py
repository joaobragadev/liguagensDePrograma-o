tempo = float(input('Digite o tempo gasto(HH:MM) : ')
velocidade = int(input('digite a velocidade  media: '))
distancia = tempo * velocidade
litros_usados = distancia / 12


print(f'o  tempo gasto foi de {tempo:.2f} horas')
print(f'A velocidade media foi de {velodade} km/h')
print(f' a distancia percorrida foi de {distancia} km')
print(f'a quantidade de combustivel foi de {litros_usados:.2f} Litros')
