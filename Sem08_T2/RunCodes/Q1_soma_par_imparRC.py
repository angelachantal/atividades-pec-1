def soma(n):
    if n % 2 == 0:
        return n + 5
    else:
        return n + 8

def main():
    n = int(input('').strip())
    
    print (soma(n))
if __name__=='__main__':
    main()