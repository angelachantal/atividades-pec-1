#Escrever um programa que leia uma determinada quantidade de minutos e informe essa quantidade convertida para horas e minutos (H:M). Por exemplo, 220 minutos é equivalente 3 horas e 40 minutos.

def horas(minutos_totais):
    return int(minutos_totais // 60)

def minutos(minutos_totais):
    return int(minutos_totais % 60)

def main():
    minutos_totais=int(input('Digite o tempo em minutos: ').strip())
    print(f'O tempo total foi de {horas(minutos_totais)}h{minutos(minutos_totais)}min.')
if __name__=='__main__':
    main()

