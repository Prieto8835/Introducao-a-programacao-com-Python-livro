#Escreva um programa que verifique se um número é palíndromo.
#Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
#Exemplos: 454, 10501
num = str(input('Digite um número: '))
print(f'Você digitou {num}')
string = num[::-1]
print(f'Número invertida fica {string}')
if num == string:
    print('Número é palíndromo! ')
else:
    print('Não é palíndromo! ')
