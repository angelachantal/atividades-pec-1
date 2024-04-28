# Escreva um programa que leia um número e exiba o dia correspondente da semana. (1-domingo, 2-segunda-feira, 3-terça-feira etc.), se digitar outro valor deve aparecer “valor inválido”.

def dia_da_semana (numero):
    if numero == 1:
        return 'domingo'
    elif numero == 2:
        return 'segunda-feira'
    elif numero == 3:
        return 'terça-feira'
    elif numero == 4:
        return 'quarta-feira'
    elif numero == 5:
        return 'quinta-feira'
    elif numero == 6:
        return 'sexta-feira'
    elif numero == 7:
        return 'sábado'
    else:
        raise ValueError ('valor inválido')

def main():
    numero = int(input('Digite o número correspondente ao dia da semana (1-domingo, 2-segunda-feira, 3-terça-feira, 4-quarta-feira, 5-quinta-feira, 6-sexta-feira, 7-sábado): \n').strip())
    
    print (dia_da_semana(numero))

if __name__=='__main__':
    main()