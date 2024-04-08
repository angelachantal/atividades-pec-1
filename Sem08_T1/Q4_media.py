# Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva os que são maiores que a média. Considere duas casas decimais.

def valor_media(n1, n2, n3, n4, n5):
    media = (n1+n2+n3+n4+n5)/5
    return(media)

def main():
    n1 = int(input('1º Número: ').strip())
    n2 = int(input('2º Número: ').strip())
    n3 = int(input('3º Número: ').strip())
    n4 = int(input('4º Número: ').strip())
    n5 = int(input('5º Número: ').strip())

    media = valor_media(n1, n2, n3, n4, n5)
    
    print (f'Média: {media:.2f}. \nNúmero(s) maior(es) que a média: ')
    
    if n1 > media:
        print (f'{n1:.2f}')
    if n2 > media:
        print (f'{n2:.2f}')
    if n3 > media:
        print (f'{n3:.2f}')
    if n4 > media:
        print (f'{n4:.2f}')
    if n5 > media:
        print (f'{n5:.2f}')
if __name__=='__main__':
    main()