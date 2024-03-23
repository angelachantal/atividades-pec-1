# Escrever um programa que leia uma temperatura em Celsius e mostre o resultado em Fahrenheit. Lembre-se:
    # °F = (°C * (9/5)) + 32
def fahrenheit(celsius):
    return float((celsius * (9/5))+32)

def main():    
    celsius = float(input('Informe a temperatura em graus Celsius: ').strip())
    print (f'A temperatura é de {fahrenheit(celsius):.2f} graus Fahrenheit.')
if __name__=='__main__':
    main()