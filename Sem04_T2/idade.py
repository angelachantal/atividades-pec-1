# Escrever um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostre na tela essa idade apenas em dias. 
# Considerar que um ano tem 365 dias e um mês tem 30 dias.

anos = int(input('Quantos anos você tem: ').strip())
meses = int(input(f'Você tem {anos} anos e quantos meses? ').strip())
dias = int(input(f'Você tem {anos} anos, {meses} meses e quantos dias? ').strip())

dias_totais = dias + (anos*365) + (meses*30)

print(f'Você tem {dias_totais} dias de vida.')