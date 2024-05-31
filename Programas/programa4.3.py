#cálculo do imposto de renda
salario = float(input('Digite seu salário para cálculo de imposto R$'))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f'Salário de R${salario:.2f} e imposto a pagar de R${imposto:.2f}')
