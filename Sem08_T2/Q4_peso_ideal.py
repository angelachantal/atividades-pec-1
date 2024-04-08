#Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para ‘homens’ e 2 para ‘mulheres’. Considerando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes fórmulas:
# para homens: (72.7 * altura) – 58
#para mulheres: (62.1 * altura) – 44.7
def peso_ideal(altura, sexo):
    if sexo == 1:
        return float((altura * 72.7) - 58)
    elif sexo == 2:
        return float((altura * 62.1) - 44.7)

def main():
    a = float(input('Altura: ').strip())
    s = int(input('Sexo (digite 1 para masculino, ou 2 para feminino): ').strip())
    
    print(f'{peso_ideal(a, s):.2f}')
if __name__=='__main__':
    main()