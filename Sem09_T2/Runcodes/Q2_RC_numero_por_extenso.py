def unidade (numero, u):
    if 0 == numero:
        return 'zero unidades'   
    elif u == 1:
        return 'uma unidade'
    elif u == 2:
        return 'duas unidades' 
    elif u == 3:
        return 'três unidades'
    elif u == 4:
        return 'quatro unidades'
    elif u == 5:
        return 'cinco unidades'
    elif u == 6:
        return 'seis unidades'
    elif u == 7:
        return 'sete unidades'
    elif u == 8:
        return 'oito unidades'
    elif u == 9:
        return 'nove unidades'

def dezena (d):
    if d == 1:
        return 'uma dezena'
    elif d == 2:
        return 'duas dezenas' 
    elif d == 3:
        return 'três dezenas'
    elif d == 4:
        return 'quatro dezenas'
    elif d == 5:
        return 'cinco dezenas'
    elif d == 6:
        return 'seis dezenas'
    elif d == 7:
        return 'sete dezenas'
    elif d == 8:
        return 'oito dezenas'
    elif d == 9:
        return 'nove dezenas'

def centena (c):
    if c == 1:
        return 'uma centena'
    elif c == 2:
        return 'duas centenas' 
    elif c == 3:
        return 'três centenas'
    elif c == 4:
        return 'quatro centenas'
    elif c == 5:
        return 'cinco centenas'
    elif c == 6:
        return 'seis centenas'
    elif c == 7:
        return 'sete centenas'
    elif c == 8:
        return 'oito centenas'
    elif c == 9:
        return 'nove centenas'

def main():
    numero = int(input(''))
    u = numero % 10
    n1 = numero // 10
    d = n1 % 10
    n1 //= 10
    c = n1 % 10
    
    if 0 <= numero < 10:
        print (f'{unidade(numero, u)}.')
    elif 10 <= numero < 100:
        if u == 0:
            print (f'{dezena(d)}.')
        else:
            print (f'{dezena(d)} e {unidade(numero, u)}.')        
    elif 100 <= numero < 1000:
        if d==0 and u == 0:
            print (f'{centena(c)}.')
        elif d != 0 and u ==0:
            print (f'{centena (c)} e {dezena(d)}.')
        elif d == 0 and u !=0:
            print (f'{centena (c)} e {unidade(numero, u)}.')
        else:
            print (f'{centena (c)}, {dezena(d)} e {unidade(numero, u)}.')
        
if __name__=="__main__":
    main()