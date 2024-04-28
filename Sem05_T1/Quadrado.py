# Escrever um programa que leia o valor do lado de um quadrado, calcule e mostre a área e o perímetro desse quadrado.
# Mostrar o resultado com 4 casas decimais, alinhado à direta, com 10 espaços na tela.

def area (l):
    return l**2

def perimetro (l):
    return 4*l

def main():
    l=float(input('Informe o valor do lado do quadrado (l): '))
    print(f'A área do quadrado é:{area(l):10.4f}')
    
    print(f'O perímetro do quadrado é:{perimetro(l):10.4f}')
    
if __name__== '__main__':
    main()