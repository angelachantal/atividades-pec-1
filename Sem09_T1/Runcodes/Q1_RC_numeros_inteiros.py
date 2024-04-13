def comparacao (n1, n2, n3):
    if n1==n2 and n2==n3:
        return 'Todos os valores são iguais'   
    else:
        return 'Todos os valores são diferentes' if (n1 != n2 and n2 != n3 and n1 !=n3) else 'Existem dois valores iguais e um diferente'

def main():
    numero1 = int(input('').strip())
    numero2 = int(input('').strip())
    numero3 = int(input('').strip())
    
    print(comparacao(numero1, numero2, numero3))
if __name__=='__main__':
    main()