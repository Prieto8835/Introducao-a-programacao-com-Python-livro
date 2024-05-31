velocidade = int(input('Digite a velocidade do carro em Km/h '))
if velocidade > 80:
    print(f'Você foi multado em R${(velocidade - 80) * 5:.2f} ')
