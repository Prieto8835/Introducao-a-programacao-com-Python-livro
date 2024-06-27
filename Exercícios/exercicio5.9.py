#Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. 
#Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números 
#como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
primeiro = num1
segundo = num2
divisão = num1 // num2
cont = 1
while cont <= divisão:
    resto = num1 - num2
    num1 = resto
    cont += 1
print(f'Divisão inteira entre {primeiro} e {segundo} é {divisão}')
print(f'Resto da divisão entre eles fica {resto}')
