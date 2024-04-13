def resto_de_5 (numero):
    resto = numero%5 
    if resto == 0:
        return 9 * numero + 7
    elif resto == 1:
        return (f'par') if numero%2==0 else (f'ímpar')
    elif resto == 2:
        return 5 * numero**2 - numero*3 + 42
    elif resto == 3:
        return numero//10
    else:
        return numero**2
            
def main():
    numero = int(input('').strip())
    
    print (resto_de_5(numero))
    
if __name__=='__main__':
    main()