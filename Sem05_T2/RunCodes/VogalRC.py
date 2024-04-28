def vogal(caractere):
    return caractere in 'aeiouAEIOU' 

def main():
    
    caractere = input().strip()
    print(f'{vogal(caractere)}')
    
if __name__=='__main__':
    main()