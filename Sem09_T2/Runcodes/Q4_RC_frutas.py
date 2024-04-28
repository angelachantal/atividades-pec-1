def morango(peso_morango):
    return peso_morango * (2.50 if peso_morango <= 5 else 2.20)

def maca(peso_maca):
    return peso_maca * (1.80 if peso_maca <= 5 else 1.50)

def valor_final(peso_total, valor_total):
    if peso_total > 8 or valor_total > 25: 
        return valor_total - (valor_total * 0.10)
    else:
        return valor_total
    
def main():
    peso_morango = float(input(''))
    peso_maca = float(input(''))
    
    peso_total = peso_morango + peso_maca
    valor_total = morango(peso_morango) + maca(peso_maca)
           
    print(f'{valor_final(peso_total, valor_total):.2f}')
    
if __name__ == '__main__':
    main()