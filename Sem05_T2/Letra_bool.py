# Escrever um programa que leia um caractere e mostre o valor booleano True (verdadeiro), se for uma LETRA (vogal ou consoante) ou o valor booleano False (falso) caso contrário.

def letra(caractere):
    return caractere in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 

def main():
    
    caractere = input('Digite um caractere: ').strip()
    print(f'Esse caractere é uma letra? {letra(caractere)}.')
    
if __name__=='__main__':
    main()