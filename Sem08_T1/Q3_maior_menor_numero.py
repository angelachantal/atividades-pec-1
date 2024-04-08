# Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes. NÃO use as funções embutidas min() e max().
def maior(n1, n2, n3, n4, n5):
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        maior = n1
    elif n2 > n3 and n2 > n4 and n2 > n5:
        maior = n2
    elif n3 > n4 and n3 > n5:
        maior = n3
    elif n4 > n5:
        maior = n4
    else:
        maior = n5
    return (maior)

def menor(n1, n2, n3, n4, n5):
    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        menor = n1
    elif n2 < n3 and n2 < n4 and n2 < n5:
        menor = n2
    elif n3 < n4 and n3 < n5:
        menor = n3
    elif n4 < n5:
        menor = n4
    else:
        menor = n5
    return (menor)

def main():
    n1 = int(input('1º Número: ').strip())
    n2 = int(input('2º Número: ').strip())
    n3 = int(input('3º Número: ').strip())
    n4 = int(input('4º Número: ').strip())
    n5 = int(input('5º Número: ').strip())

    print (f'Número maior: {maior(n1, n2, n3, n4, n5)} \nNúmero Menor: {menor(n1, n2, n3, n4, n5)}')
if __name__=='__main__':
    main()