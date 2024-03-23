#Você foi ao mercado mágico e, ao comprar 3 maçãs e 2 bananas, o caixa precisa da sua ajuda para calcular o total! Leia o preço de uma maçã e o preço de uma banana, calcule e imprima o total da sua compra.

def maca(prc_maca, qtd=3):
    return prc_maca*qtd

def banana(prc_banana, qtd=2):
    return prc_banana*qtd

def main():
    
    prc_maca=float(input('Preço da maçã: ').strip())
    prc_banana=float(input('Preço da banana: ').strip())
    total = maca(prc_maca)+banana(prc_banana)
    print(f'O valor total de 3 maças e 2 bananas é: {total:.2f}.')
    
if __name__=='__main__':
    main()
