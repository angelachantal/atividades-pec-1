# Escrever um programa que leia uma temperatura em graus Celsius e mostre na tela o valor correspondente em graus Fahrenheit.
# Considerar que: Fahrenheit = (Celsius x (9 / 5)) + 32

celsius = float(input('Informe a temperatura em graus Celsius: ').strip())
Fahrenheit = float((celsius * (9/5))+32)
print (f'A temperatura é de {Fahrenheit:.2f} graus Fahrenheit.')