def n_maior (a, b, c, d, e):
    return max(a, b, c, d, e)

def n_menor (a, b, c, d, e):
    return min(a, b, c, d, e)

def media (a, b, c, d, e):
    import statistics
    return statistics.mean([a, b, c, d, e])

def main():
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    d = int(input().strip())
    e = int(input().strip())
    
    print (f'{n_maior (a, b, c, d, e)}')
    print (f'{n_menor (a, b, c, d, e)}')
    print (f'{media (a, b, c, d, e)}')
    
if __name__=='__main__':
    main()