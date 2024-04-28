# Escrever um programa que leia um caractere e mostre o valor booleano True (verdadeiro), se for um SÍMBOLO (o que não é letra ou número), ou o valor booleano False (falso), caso contrário.

def simbolo(caractere):
    return not (caractere in 'aeiouyAEIOUYbcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ0123456789')

def main():
    
    caractere = input('Digite um caractere: ').strip()
    print(f'Esse caractere é uma símbolo? {simbolo(caractere)}.')
    
if __name__=='__main__':
    main()