# Escreva um programa que leia dois valores que correspondem à base e à altura de um retângulo. O programa deve inicialmente verificar se os valores formam um retângulo ou um quadrado. Caso formem um quadrado imprima a palavra QUADRADO e caso seja um retângulo, mostre o perímetro (soma de todos os lados) e a área (base vezes a altura) do retângulo. Separe esses valores com um hífen.

def retangulo (base, altura):
    if base == altura:
        return 'É um QUADRADO.'
    else:
        return (f'Perímetro = {2*base + 2* altura} - Área = {base * altura}')

def main():
    base = int(input('Base do retângulo: ').strip())
    altura = int(input('Altura do retângulo: ').strip())
    
    print (retangulo(base, altura))
    
if __name__=='__main__':
    main()