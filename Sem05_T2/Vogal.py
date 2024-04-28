# Escrever um programa que leia um caractere e mostre o valor booleano True (verdadeiro), se for uma VOGAL, ou False (falso), caso contrário.

def vogal(caractere):
    return caractere in 'aeiouAEIOU' 

def main():
    
    caractere = input('Digite um caractere: ').strip()
    print(f'Esse caractere é uma vogal? {vogal(caractere)}.')
    
if __name__=='__main__':
    main()