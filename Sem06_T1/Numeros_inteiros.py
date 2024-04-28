# Escreva um programa/algoritmo que leia 5 (cinco) números inteiros e escreva na tela:
    #• o maior número lido;
    #• o menor número lido;
    #• a média aritmética dos números lidos.
def n_maior (a, b, c, d, e):
    return max(a, b, c, d, e)

def n_menor (a, b, c, d, e):
    return min(a, b, c, d, e)

def media (a, b, c, d, e):
    import statistics
    return statistics.mean([a, b, c, d, e])

def main():
    a = int(input('a = ').strip())
    b = int(input('b = ').strip())
    c = int(input('c = ').strip())
    d = int(input('d = ').strip())
    e = int(input('e = ').strip())
    
    print (f'O maior número é {n_maior (a, b, c, d, e)}')
    print (f'O menot número é {n_menor (a, b, c, d, e)}')
    print (f'A média aritmética dos números é {media (a, b, c, d, e)}')
    
if __name__=='__main__':
    main()