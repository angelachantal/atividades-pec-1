def simbolo(caractere):
    return not (caractere in 'aeiouyAEIOUYbcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ0123456789')

def main():
    
    caractere = input().strip()
    print(f'{simbolo(caractere)}')
    
if __name__=='__main__':
    main()