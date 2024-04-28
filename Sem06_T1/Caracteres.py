# Escrever um programa que leia um nome pelo teclado e informe quantos caracteres o nome possui.

def caracteres (nome):
    return len(nome)

def main ():
    nome=input('Nome: ').strip()
    print (caracteres(nome))
if __name__ == '__main__':
    main()

