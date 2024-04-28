# Escreva um programa que leia um caractere e mostre o valor booleano True (verdadeiro), se for uma LETRA (vogal ou consoante) ou um NÚMERO (entre ‘0’ e ‘9’), ou valor booleano False (falso) caso contrário.
def letra_numero(caractere):
    return caractere in 'aeiouyAEIOUYbcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ0123456789' 

def main():
    
    caractere = input('Digite um caractere: ').strip()
    print(f'Esse caractere é uma consoante? {letra_numero(caractere)}.')
    
if __name__=='__main__':
    main()