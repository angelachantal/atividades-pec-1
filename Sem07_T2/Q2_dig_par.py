# Escreva um programa que leia um número inteiro entre 100 e 999, mostre quantos dígitos pares existem nesse número. Por exemplo: 245 tem 2 dígitos pares; 135 tem 0 dígitos pares; 134 tem 1 dígito par.

def pares(n):
    if n % 2 == 0:
        return 1
    else:
        return 0

def main():
    numero = int(input('Digite um número de 100 a 999: ').strip())
    c = numero//100
    d = (numero%100)//10
    u = (numero%100) %10
    if c !=0:
        soma_pares = pares(c) + pares(d) + pares (u)
    elif c == 0 and d != 0:
        soma_pares = pares(d) + pares (u)
    elif c == 0 and d == 0:
        soma_pares = pares (u)
        
    print(soma_pares)    
if __name__=='__main__':
    main()