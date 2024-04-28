#Um sacolão está vendendo frutas com a seguinte tabela de preços:
# Até 5Kg:
    # Morango - R$ 2,50 por Kg
    # Maça - R$ 1,80 por Kg
# Acima de 5Kg 
    # Morango - R$ 2,20 por Kg
    # Maça - R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um programa que leia a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

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
    peso_morango = float(input('Morango (Kg): '))
    peso_maca = float(input('Maçã (kg): '))
    
    peso_total = peso_morango + peso_maca
    valor_total = morango(peso_morango) + maca(peso_maca)
           
    print(f'O valor final da compra é: R${valor_final(peso_total, valor_total):.2f}')
    
if __name__ == '__main__':
    main()