# Escreva um programa que leia uma data no formado DDMMAAA e informe se é uma data válida.
# OBS: Use apenas condicionais e os tipos básicos do Python; Não utilize bibliotecas do Python que tratam datas; Considere que em anos bissextos o mês de fevereiro tem 29 dias.

def separar_data (data):
    aa = data % 10000
    data //= 10000
    mm = data % 100
    data //= 100
    dd = data
    
    if mm == 2:
        if (aa % 4 == 0 and aa % 100 != 0) or (aa % 400 == 0):
            return aa > 0 and 12 >= mm > 0 and 29 >= dd > 0
        else:
            return aa > 0 and 13 > mm > 0 and 28 >= dd > 0        
    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
        return aa > 0 and 12 >= mm > 0 and 30 >= dd > 0
    else:
        return aa > 0 and 12 >= mm > 0 and 31 >= dd >0       
        
def main():
    data = int(input('Digite a data no formato DDMMAAAA: '))
    print (separar_data(data))
if __name__=='__main__':
    main()