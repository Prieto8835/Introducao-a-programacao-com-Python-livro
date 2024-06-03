#Escreva um programa que leia três números e que imprima o maior e o menor.
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
"""maior = menor = 0
if num1 > num2 and num1 >num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print(f'Maior valor é o {maior} e o menor é o {menor} ')"""
maior = menor = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
print(f'Maior valor digitado foi {maior} e o menor foi {menor} ')
