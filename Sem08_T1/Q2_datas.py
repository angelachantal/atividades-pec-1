# Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.
def data(dia, mes, ano):
    data = str(dia) + '/' + str(mes) + '/' + str(ano)
    return (data)

def main():
    dia1 = int(input('Dia 1: ').strip())
    mes1 = int(input('Mês 1: ').strip())
    ano1 = int(input('Ano 1: ').strip())
    data1 = data(dia1, mes1, ano1)
    
    dia2 = int(input('Dia 2: ').strip())
    mes2 = int(input('Mês 2: ').strip())
    ano2 = int(input('Ano 2: ').strip())
    data2 = data(dia2, mes2, ano2)

    if ano2 > ano1: 
        print (f'Data mais recente: {data2}')
    elif ano2==ano1 and mes2>mes1:
        print (f'Data mais recente: {data2}')
    elif ano2==ano1 and mes2==mes1 and dia2>dia1:
        print (f'Data mais recente: {data2}')
    else:
        print (f'Data mais recente: {data1}')
if __name__=='__main__':
    main()