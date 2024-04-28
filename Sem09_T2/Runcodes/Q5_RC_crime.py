def pontuacao(pergunta1, pergunta2, pergunta3, pergunta4, pergunta5):
    pont = 0
    if pergunta1 == 'S':
        pont += 1
    if pergunta2 == 'S':
        pont += 1
    if pergunta3 == 'S':
        pont += 1
    if pergunta4 == 'S':
        pont += 1
    if pergunta5 == 'S':
        pont += 1
    return pont

def classificacao (pont):
    
    if pont == 2:
        return 'Suspeito'
    elif pont == 3 or pont == 4:
        return 'Cúmplice'
    elif pont == 5:
        return 'Assassino'
    else:
        return 'Inocente'
    
def main():
    pergunta1 = input("").strip().upper()
    pergunta2 = input("").strip().upper()
    pergunta3 = input("").strip().upper()
    pergunta4 = input("").strip().upper()
    pergunta5 = input("").strip().upper()

    pont = pontuacao(pergunta1, pergunta2, pergunta3, pergunta4, pergunta5)
    
    print(f'{classificacao(pont)}')
    
if __name__ == '__main__':
    main()