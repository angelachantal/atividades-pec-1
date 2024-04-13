#Escrever um programa que leia 3 valores inteiros. Determinar se é o segundo ou o terceiro valor lido que possui menor diferença com relação ao primeiro, imprimindo o valor da diferença.

def diferenca(n1, n2, n3):
    return abs(n2-n1) if abs(n2-n1) < abs(n3-n1) else abs(n3-n1)

def main():
    numero1 = int(input('Digite o primeiro número: ').strip())
    numero2 = int(input('Digite o segundo número: ').strip())
    numero3 = int(input('Digite o terceiro número: ').strip())
    
    print (diferenca(numero1, numero2, numero3))
    
if __name__=='__main__':
    main()