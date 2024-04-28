def area (l):
    return l**2

def perimetro (l):
    return 4*l

def main():
    l=float(input())
    print(f'{area(l):10.4f}')
    
    print(f'{perimetro(l):10.4f}')
    
if __name__== '__main__':
    main()