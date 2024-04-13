def operacoes(n1, n2, op):
    if op == 1:
        resultado = n1+n2
    elif op == 2:
        resultado = n1-n2
    elif op == 3:
        resultado = n1*n2
    elif op == 4:
        resultado = n1/n2
    else:
        raise ValueError('')
    return resultado

def main():
    numero1 = int(input('').strip())
    numero2 = int(input('').strip())
    operacao = int(input('').strip())
    
    resultado = operacoes(numero1, numero2, operacao)
    
    print(f'{resultado}')
if __name__=='__main__':
    main()