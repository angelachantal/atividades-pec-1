# Escreva um programa que leia um número inteiro e calcule o resto da divisão inteira do número lido por 5 (cinco). A seguir, de acordo com o resultado da divisão, faça o que é solicitado abaixo:
    # Se 0 (zero), escreva a o resultado da equação 9n + 7, onde n é o valor lido;
    # Se 1 (um), escreva se o valor lido é par ou ímpar;
    # Se 2 (dois), escreva a o resultado da equação 5n² – 3n + 42, onde n é o valor lido;
    # Se 3 (três), escreva a divisão inteira do valor lido por 10;
    # Se 4 (quatro), escreva o quadrado do valor lido.
    
    
def resto_de_5 (numero):
    resto = numero%5 
    if resto == 0:
        return (f' 9 * {numero} + 7 = {9*numero + 7}')
    elif resto == 1:
        return (f'{numero} é par') if numero%2==0 else (f'{numero} é ímpar')
    elif resto == 2:
        return (f' 5 * {numero}² – 3 * {numero} + 42 = {5 * numero**2 - numero*3 + 42}')
    elif resto == 3:
        return (f'{numero}//10 = {numero//10}')
    else:
        return (f'{numero} ** 2 = {numero**2}')
            
def main():
    numero = int(input('Digite um número: ').strip())
    
    print (resto_de_5(numero))
if __name__=='__main__':
    main()