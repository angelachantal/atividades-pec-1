# Escreva um programa que leia um único caractere pelo teclado e informe o código numérico correspondente ao caractere lido.

def unicode(caractere):
    return ord(caractere)

def main():
    caractere = input('Digite um caractere: ').strip()
    print(unicode(caractere))
if __name__=='__main__':
    main()
