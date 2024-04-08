#Escreva um programa que leia um número inteiro e some 5 caso valor lido seja par ou some 8 caso o valor lido seja ímpar. Mostre na tela o resultado da operação.
def soma(n):
    if n % 2 == 0:
        return n + 5
    else:
        return n + 8

def main():
    n = int(input('Digite um número: ').strip())
    
    print (soma(n))
if __name__=='__main__':
    main()