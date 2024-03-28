# Escrever um programa que leia três números correspondentes a três notas de um aluno e apresente a média das três notas. Mas se a terceira nota for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso, se a média final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.

def med(n1, n2, n3):
    media = (n1+n2+n3)/3
    if n3 > 8:
        return media + 1
    else:
        return media
def med_final(media):
    if media>10:
        return 10
    else:
        return media
def main():
    n1 = float(input('Nota 1: ').strip())
    n2 = float(input('Nota 2: ').strip())
    n3 = float(input('Nota 3: ').strip())
    media= med(n1,n2,n3)
    print (f'Média: {med_final(media):.2f}')
if __name__=='__main__':
    main()