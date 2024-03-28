# Escrever um programa que leia um número e mostre o valor booleano True (verdadeiro), se for ímpar; ou o valor booleano False (falso), caso contrário.
def eh_impar(numero):
    return numero % 2 != 0
def main():
    numero = int(input('Número: '))
    print (f'O número é par? {eh_impar(numero)}.')
if __name__=='__main__':
    main()