def diferenca(n1, n2, n3):
    return abs(n2-n1) if abs(n2-n1) < abs(n3-n1) else abs(n3-n1)

def main():
    numero1 = int(input('').strip())
    numero2 = int(input('').strip())
    numero3 = int(input('').strip())
    
    print (diferenca(numero1, numero2, numero3))
    
if __name__=='__main__':
    main()