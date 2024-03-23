
def minutos_para_horas (qtd_minutos):
    
    horas = qtd_minutos // 60
    
    minutos =qtd_minutos % 60
    
    return f'{horas}h{minutos}min'


minutos = int(input('Quantidade de minutos: '))

horas = minutos_para_horas(minutos)

print(f'{minutos} minutos são equivalentes a {horas}') 