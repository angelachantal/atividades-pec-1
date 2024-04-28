def letra_numero(caractere):
    return caractere in 'aeiouyAEIOUYbcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ0123456789' 

def main():
    
    caractere = input().strip()
    print(f'{letra_numero(caractere)}')
    
if __name__=='__main__':
    main()