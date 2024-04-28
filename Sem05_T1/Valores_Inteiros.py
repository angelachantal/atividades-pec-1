# Escrever um programa que leia três valores inteiros e calcule o valor da função "calcular":
# def calcular(a, b,c):
#     return 2 * a + 5 * b - c

def calcular (a, b, c):
    return 2*a+5*b-c

def main():
    a = int(input('Informe o valor de a: '). strip())
    b = int(input('Informe o valor de b: '). strip())
    c = int(input('Informe o valor de c: '). strip())

    print(f'O resultado da função é: {calcular(a,b,c)}')
    
if __name__== '__main__':
    main()