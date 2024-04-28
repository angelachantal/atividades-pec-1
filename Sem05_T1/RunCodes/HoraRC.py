def horas(minutos_totais):
    return int(minutos_totais // 60)

def minutos(minutos_totais):
    return int(minutos_totais % 60)

def main():
    minutos_totais=int(input().strip())
    print(f'{horas(minutos_totais)}:{minutos(minutos_totais)}')
          
if __name__=='__main__':
    main()