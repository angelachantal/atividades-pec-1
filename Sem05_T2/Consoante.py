# Escrever um programa que leia um caractere e mostre o valor booleano True (verdadeiro), se for uma CONSOANTE, ou o valor booleano False (falso), caso contrário.

def consoante(caractere):
    return caractere in 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ' 

def main():
    
    caractere = input('Digite um caractere: ').strip()
    print(f'Esse caractere é uma consoante? {consoante(caractere)}.')
    
if __name__=='__main__':
    main()