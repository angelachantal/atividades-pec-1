def aumento (preco, percentual):
    percentual = percentual/100
    return preco +(percentual*preco)

def desconto (preco, percentual):
    percentual = percentual/100
    return preco -(percentual*preco)

def main():
    preco=float(input().strip())
    percentual=float(input().strip())
    
    print(f'{aumento(preco,percentual):.2f}')
    
    print(f'{desconto(preco,percentual):.2f}')
if __name__== '__main__':
    main()