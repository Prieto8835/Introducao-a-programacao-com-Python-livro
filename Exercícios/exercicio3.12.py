#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a 
#velocidade média esperada para a viagem.

distancia = (float(input('Distância da viagem em Km: ')))
velocidade = (float(input('Velocidade média da viagem em Km/h ')))
print(f'Estimativa de chegada é de {distancia / velocidade:.2f} horas')
