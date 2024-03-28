# Escrever um programa que leia o nome e o sexo de uma pessoa, e mostre o nome precedido da mensagem “Ilmo Sr.”, caso seja do sexo masculino (1), ou “Ilma Sra.”, se for do sexo feminino (2).

def vocativo(sexo):
    if sexo == 1:
        return ('Ilmo Sr.')
    else:
        return ('Ilma Sra.')
    
def main():
    nome = input(). strip()
    sexo = int(input().strip())
    print(f'{vocativo(sexo)} {nome}')
    
if __name__=='__main__':
    main()