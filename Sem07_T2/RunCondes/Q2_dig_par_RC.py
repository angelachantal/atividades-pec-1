def pares(n):
    if n % 2 == 0:
        return 1
    else:
        return 0

def main():
    numero = int(input().strip())
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