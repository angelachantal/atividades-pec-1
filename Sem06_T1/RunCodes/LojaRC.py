def desconto(preco, percentual=0.09):
    return preco-(percentual*preco)

def etiqueta(preco):
    return preco/5

def juros(preco, percentual=0.17):
    return (preco +(percentual*preco))/10

def main():
    preco = float(input().strip())
    print(f'{desconto(preco):.2f}', f'{etiqueta(preco):.2f}', f'{juros(preco):.2f}', sep='\n')
if __name__=="__main__":
    main()