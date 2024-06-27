#Escreva um programa que calcule o resto da divisão inteira entre dois números. 
#Utilize apenas as operações de soma e subtração para calcular o resultado.
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
divisão = num1 //num2
cont = 1
while cont <= divisão:
    resultado = num1 - num2
    num1 = resultado
    cont += 1
print(f'Valor da divisão exata é {divisão}')
print(f'Resto da divisão: {resultado}')
