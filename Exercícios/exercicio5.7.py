#Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
começo = int(input('Digite valor inicial da tabuada: '))
fim = int(input('Digite valor final da tabuada: '))
num = int(input('Digite o valor para tabuada: '))
while começo <= fim:
    print(f'{num} x {começo} = {num * começo} ')
    começo += 1
