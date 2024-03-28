def eh_impar(numero):
    return numero % 2 != 0
def main():
    numero = int(input())
    print (f'{eh_impar(numero)}')
if __name__=='__main__':
    main()