def data(dia, mes, ano):
    data = str(dia) + '/' + str(mes) + '/' + str(ano)
    return (data)

def main():
    dia1 = int(input().strip())
    mes1 = int(input('').strip())
    ano1 = int(input('').strip())
    data1 = data(dia1, mes1, ano1)
    
    dia2 = int(input('').strip())
    mes2 = int(input('').strip())
    ano2 = int(input('').strip())
    data2 = data(dia2, mes2, ano2)

    if ano2 > ano1: 
        print (f'{data2}')
    elif ano2==ano1 and mes2>mes1:
        print (f'{data2}')
    elif ano2==ano1 and mes2==mes1 and dia2>dia1:
        print (f'{data2}')
    else:
        print (f'{data1}')
if __name__=='__main__':
    main()