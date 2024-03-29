def n_maior(n1, n2, n3):
    return max(n1, n2, n3)
    
def n_menor(n1, n2, n3):
    return min(n1, n2, n3)

def n_meio(n1, n2, n3):
    if ((n1 != n_maior(n1, n2, n3)) and (n1 != n_menor(n1, n2, n3))):
        return n1
    elif ((n2 != n_maior(n1, n2, n3)) and (n2 != n_menor(n1, n2, n3))):
        return n2
    elif ((n3 != n_maior(n1, n2, n3)) and (n3 != n_menor(n1, n2, n3))):
        return n3
    
def main():
    n1 = input().strip()
    n2 = input().strip()
    n3 = input().strip()
    
    print (f'{n_menor(n1, n2, n3)} \n{n_meio(n1, n2, n3)} \n{n_maior(n1, n2, n3)}')
if __name__ == '__main__':
    main()