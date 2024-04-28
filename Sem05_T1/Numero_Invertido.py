#Ler um número inteiro entre 1000 e 9999 e mostrá-lo na ordem inversa. 
# Por exemplo, se o número lido for 5678 deverá ser mostrado 8765.

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
    
    numero=int(input('Digite um número inteiro de 1000 a 9999: ').strip())
    print (f'Esse número, invertido, fica: {numero_invertido(numero)}.')
    
if __name__=='__main__':
    main()