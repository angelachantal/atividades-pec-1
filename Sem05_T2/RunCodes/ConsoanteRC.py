def consoante(caractere):
    return caractere in 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ' 

def main():
    
    caractere = input('').strip()
    print(f'{consoante(caractere)}')
    
if __name__=='__main__':
    main()