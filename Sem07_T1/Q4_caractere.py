# Escrever um programa que leia um caractere e mostre uma das seguintes mensagens: “vogal”, “consoante”, “número” ou “símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros devem ser considerados símbolos.
def classif(caract):
    if caract in ('aeiouyAEIOUY'):
        return 'Vogal'
    elif caract in ('bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'):
        return 'Consoante'
    elif caract in ('0123456789'):
        return 'Número'
    else:
        return 'Símbolo'
    
def main():
    caract = input('Caractere: ')
    print (f'Classificação: {classif(caract)}')
if __name__=='__main__':
    main()