#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular 
#soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operação = int(input(f'Selecione uma operação matemática para fazer com os números {num1} e {num2}:\n[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Divisão \nSua opção: '))
if operação == 1:
    print(f'Soma de {num1} + {num2} = {num1 + num2} ')
elif operação == 2:
    print(f'Subtração de {num1} - {num2} = {num1 - num2} ')
elif operação == 3:
    print(f'Multiplicação de {num1} x {num2} = {num1 * num2} ')
elif operação == 4:
    print(f'Divisão de {num1} / {num2} = {num1 / num2:.2f} ')
else:
    print('Opção inválida! Selecione uma entre 1 e 4. ')
