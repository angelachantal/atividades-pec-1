# Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o número lido.
# Nenhum dígito é ímpar.
# Apenas um dígito é ímpar.
# Os dois dígitos são ímpares.
    
def soma_pares (d, u):
    if (d % 2 == 0) and (u % 2 == 0):
        return 'Nenhum dígito é ímpar.'
    elif ((d % 2 != 0) and (u % 2 == 0) or ((d % 2 == 0) and (u % 2 != 0))):
        return 'Apenas um dígito é ímpar.'
    elif (d % 2 != 0) and (u % 2 != 0):
        return 'Os dois dígitos são ímpares.' 
def main():
    numero = int(input('Digite um número de 10 a 99: ').strip())
    d = numero//10
    u = numero%10
    print(soma_pares(d,u))   
if __name__=='__main__':
    main()