
def trocar(x1, x2):
    
    return x2, x1

n1 = int(input('Primeiro número: '))

n2 = int(input('Segundo número: '))

n1, n2 = trocar(n1, n2)

print(f'Primeiro {n1}; Segundo {n2}.') 