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
    n1 = int(input('').strip())
    n2 = int(input('').strip())
    n3 = int(input('').strip())
    n4 = int(input('').strip())
    n5 = int(input('').strip())

    print (f'{maior(n1, n2, n3, n4, n5)} \n{menor(n1, n2, n3, n4, n5)}')
if __name__=='__main__':
    main()