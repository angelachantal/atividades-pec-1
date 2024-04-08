def peso_ideal(altura, sexo):
    if sexo == 1:
        return float((altura * 72.7) - 58)
    elif sexo == 2:
        return float((altura * 62.1) - 44.7)

def main():
    a = float(input('').strip())
    s = int(input('').strip())
    
    print(f'{peso_ideal(a, s):.2f}')
if __name__=='__main__':
    main()