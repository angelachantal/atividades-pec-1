def retangulo (base, altura):
    if base == altura:
        return 'QUADRADO'
    else:
        return (f'{2*base + 2* altura} - {base * altura}')

def main():
    base = int(input('').strip())
    altura = int(input('').strip())
    
    print (retangulo(base, altura))
    
if __name__=='__main__':
    main()