#Escrever um programa que leia um valor inteiro e mostre na tela no valor booleano True caso o número lido seja maior que 100 
# ou False caso contrário.

numero = int(input('Digite um número: ').strip())

if numero > 100:
    print(True)
else:
    print(False)