#Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:
#     9 × C
# F = ----- + 32
#       5

temperatura = int(input('Digite a temperatura em °C para conversão: '))
print(f'Convertido em °F fica: {(9 * temperatura / 5) + 32}')
