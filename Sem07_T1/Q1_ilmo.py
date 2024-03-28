# Escrever um programa que leia o nome e o sexo de uma pessoa, e mostre o nome precedido da mensagem “Ilmo Sr.”, caso seja do sexo masculino (1), ou “Ilma Sra.”, se for do sexo feminino (2).

def vocativo(sexo):
    if sexo == 1:
        return ('Ilmo Sr.')
    else:
        return ('Ilma Sra.')
    
def main():
    nome = input('Nome: '). strip()
    sexo = int(input('Sexo (digite 1 para masculino, ou 2 para feminino): ').strip())
    print (f'{vocativo(sexo)} {nome}')
    
if __name__=='__main__':
    main()