#Você é dono de uma loja que vende roupas. Sua política é de dar desconto para quem compra à vista, vender pelo preço de etiqueta para quem paga em 5 vezes e cobrar juros de quem comprar em 10 vezes. Escreva um programa que leia o valor de uma compra e imprima três valores, todos com até duas casas decimais:
    #• Valor para pagamento à vista, com desconto de 9%.
    #• Valor da prestação para pagamento em 5 vezes, sem desconto nem juros.
    #• Valor da prestação para pagamento em 10 vezes, com 17% de juros.
    
def desconto(preco, percentual=0.09):
    return preco-(percentual*preco)

def etiqueta(preco):
    return preco/5

def juros(preco, percentual=0.17):
    return (preco +(percentual*preco))/10

def main():
    preco = float(input('Valor da compra: ').strip())
    print(f'Pagamento à vista: R$ {desconto(preco):.2f}', f'Parcelado em até 5 vezes: R$ {etiqueta(preco):.2f}', f'Parcelado em 10 vezes: R$ {juros(preco):.2f}', sep='\n')
if __name__=="__main__":
    main()