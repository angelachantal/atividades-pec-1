def numero_invertido(numero):
    unid = numero%10
    
    numero = numero//10
    dez = numero%10
    
    numero = numero//10
    cen = numero%10
    
    numero = numero//10
    mil = numero%10
    
    return (unid*1000)+(dez*100)+(cen*10)+ mil
    
def main():
    
    numero=int(input().strip())
    print (numero_invertido(numero))
    
if __name__=='__main__':
    main()