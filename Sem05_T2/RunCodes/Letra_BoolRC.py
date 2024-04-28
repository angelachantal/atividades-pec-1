def letra(caractere):
    return caractere in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 

def main():
    
    caractere = input().strip()
    print(f'{letra(caractere)}')
    
if __name__=='__main__':
    main()