# Escrever um programa que leia o nome e o estado civil de uma pessoa (1 - casado, 2 - solteiro). Se a pessoa for casada, leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s) nome(s) lido(s).

def caract(nome, est_civil):
    if est_civil==1:
        conjuge = input().strip()
        return len(nome) + len(conjuge)
    else:
        return len(nome)

def main():
    nome = input().strip()
    est_civil = int(input())
    print(f'{caract(nome, est_civil)}')
if __name__ == '__main__':
    main()