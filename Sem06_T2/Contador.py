# Fazer um contador de letras. Peça ao usuário para digitar uma frase qualquer e, em seguida, imprima o número de caracteres nessa frase sem considerar espaços em branco no início ou final da frase digitada.

def caracteres(frase):
    return len(frase)

def main():
    frase=input('Digite uma frase: ').strip()
    print(f'A frase "{frase}" possui {caracteres(frase)} caracteres.')
if __name__=='__main__':
    main()