#Escreva um programa que leia um número inteiro. Mostre a soma dos dígitos se o valor lido for entre 0 (zero) e 100 mil ou -1 (menos um) para outros valores. Exemplo: 12.476 deve mostrar a 20.
def soma_digitos(n):
    if n >= 0 and n < 100000:
        cm = n // 100000
        n %= 100000
        
        dm = n // 10000
        n %= 10000
        
        m = n // 1000
        n %= 1000
        
        c = n // 100
        n %= 100
        
        d = n //10
        n %= 10
        
        u = n
        
        return u + d + c + m + dm + cm
        
    else:
        return '-1'

def main():
    n = int(input('Digite um número inteiro entre 0 e 100.000: ').strip())
    
    print (soma_digitos(n))
if __name__=='__main__':
    main()