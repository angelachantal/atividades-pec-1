#O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal. O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa está em quilogramas e a altura em metros. Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e calcula o IMC de uma pessoa, e depois, mostra uma das seguintes mensagens:

def icm (m, a):
    icm = float(m/(a**2))
    print (f'ICM: {icm:.2f}')

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
    m = float(input('Massa (Kg): ').strip())
    a = float(input('Altura (m): ').strip())
    
    print(f'Classificação: {icm(m, a)}')
if __name__=='__main__':
    main()