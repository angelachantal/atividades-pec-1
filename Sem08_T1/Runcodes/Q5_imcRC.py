def icm (m, a):
    icm = float(m/(a**2))
    print (f'{icm:.2f}')
    
    if icm < 18.5:
        return ('Abaixo do peso')
    if icm < 25:
        return ('Peso normal')
    if icm < 30:
        return ('Sobrepeso')
    if icm < 35:
        return ('Obeso leve')
    if icm < 40:
        return ('Obeso moderado')
    if icm >= 40:
        return ('Obeso mórbido')
        
def main():
    m = float(input('').strip())
    a = float(input('').strip())
    
    print(f'{icm(m, a)}')
if __name__=='__main__':
    main()