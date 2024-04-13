# Escrever um programa que leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcular e mostrar o resultado dessa operação sobre os dois valores lidos.

def operacoes(n1, n2, op):
    if op == 1:
        resultado = n1+n2
    elif op == 2:
        resultado = n1-n2
    elif op == 3:
        resultado = n1*n2
    elif op == 4:
        resultado = n1/n2
    else:
        raise ValueError('Tente novamente e digite um número válido para a operação: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão')
    return resultado

def main():
    numero1 = int(input('Digite o primeiro número: ').strip())
    numero2 = int(input('Digite o segundo número: ').strip())
    operacao = int(input('Digite o número correspondente à operação que deseja executar ( 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão): ').strip())
    
    resultado = operacoes(numero1, numero2, operacao)
    
    print(f'O resultado da operação é {resultado}.')
if __name__=='__main__':
    main()