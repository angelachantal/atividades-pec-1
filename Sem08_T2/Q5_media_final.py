#Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3 provas e a média das notas obtidas nos exercícios que fazem parte da sua avaliação.
#O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente e a mensagem “Aprovado” se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.
def conceito(media_final):
    if media_final >= 9.0:
        return "A - Aprovado"
    elif 7.5 <= media_final < 9.5:
        return 'B - Aprovado'
    elif 6.0 <= media_final < 7.5:
        return 'C - Aprovado'
    elif 4.0 <= media_final < 6.0:
        return 'D - Reprovado'
    elif media_final < 4.0:
        return 'E - Reprovado'

def main():
    matricula = input('Matrícula: ').strip()
    nota1 = float(input('Nota 1: ').strip())
    nota2 = float(input('Nota 1: ').strip())
    nota3 = float(input('Nota 1: ').strip())
    #media = (nota1 + nota2 + nota3)/3
    media = float(input('Média: ').strip())
    
    media_final = (nota1 + nota2 * 2 + nota3 * 3 + media)/7
    
    print(f'Matrícula: {matricula}git inoit \nMédia Final: {media_final:.2f} \nResultado: {conceito(media_final)}')
if __name__=='__main__':
    main()