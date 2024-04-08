def conceito(media_final):
    if media_final >= 9.0:
        return (f'A \nAprovado')
    elif 7.5 <= media_final < 9.5:
        return (f'B \nAprovado')
    elif 6.0 <= media_final < 7.5:
        return (f'C \nAprovado')
    elif 4.0 <= media_final < 6.0:
        return (f'D \nReprovado')
    elif media_final < 4.0:
        return (f'E \nReprovado')

def main():
    matricula = input('').strip()
    nota1 = float(input('').strip())
    nota2 = float(input('').strip())
    nota3 = float(input('').strip())
    media = float(input('').strip())
    
    media_final = (nota1 + nota2 * 2 + nota3 * 3 + media)/7
    
    print (matricula)
    print(f'{media_final:.2f}')
    print(f'{conceito(media_final)}')
if __name__=='__main__':
    main()