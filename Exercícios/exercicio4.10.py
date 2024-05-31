num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
operação = int(input(f'Selecione uma operação matemática para fazer com os números {num1} e {num2}:\n[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Divisão \nSua opção: '))
if operação == 1:
    print(f'Soma de {num1} + {num2} = {num1 + num2} ')
elif operação == 2:
    print(f'Subtração de {num1} - {num2} = {num1 - num2} ')
elif operação == 3:
    print(f'Multiplicação de {num1} x {num2} = {num1 * num2} ')
elif operação == 4:
    print(f'Divisão de {num1} / {num2} = {num1 / num2} ')
else:
    print('Opção inválida! Selecione uma entre 1 e 4. ')
