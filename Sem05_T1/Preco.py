# Escrever um programa que leia um preço e um valor percentual e informe o preço acrescido do percentual e o preço com o desconto percentual, com duas casas decimais
# Por exemplo, se for lido um preço de 100.00 e um valor percentual de 5.00, o programa deve mostrar que o preço com aumento é 105.00 e o preço com desconto é 95.00.

def aumento (preco, percentual):
    percentual = percentual/100
    return preco +(percentual*preco)

def desconto (preco, percentual):
    percentual = percentual/100
    return preco -(percentual*preco)

def main():
    preco=float(input('Valor do produto: R$ ').strip())
    percentual=float(input('Percentual de aumento/desconto: ').strip())
    
    print(f'O valor do produto com aumento é de R$ {aumento(preco,percentual):.2f}.')
    
    print(f'O valor do produto com desconto é de R$ {desconto(preco,percentual):.2f}.')
if __name__== '__main__':
    main()