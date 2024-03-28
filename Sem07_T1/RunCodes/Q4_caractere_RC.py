# Escrever um programa que leia um caractere e mostre uma das seguintes mensagens: “vogal”, “consoante”, “número” ou “símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros devem ser considerados símbolos.
def classif(caract):
    if caract in ('aeiouyAEIOUY'):
        return 'vogal'
    elif caract in ('bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'):
        return 'consoante'
    elif caract in ('0123456789'):
        return 'número'
    else:
        return 'símbolo'
    
def main():
    caract = input()
    print (f'{classif(caract)}')
if __name__=='__main__':
    main()