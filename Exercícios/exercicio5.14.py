#Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). 
#No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
cont = soma = 0
while True:
    num = int(input('Digite um valor, digite 0 para parar: '))
    soma += num
    if num == 0:
        break
    cont += 1
print(f'Com {cont} números digitados, a soma dos valores digitados é {soma} e a média aritimética é {soma / cont:.2f} ')
