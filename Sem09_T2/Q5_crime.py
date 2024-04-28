# Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    #a) 'Telefonou para a vítima ?'
    #b) 'Esteve no local do crime ?'
    #c) 'Mora perto da vítima ?'
    #d) 'Devia para a vítima ?'
    #e) 'Já trabalhou com a vítima ?'
#Considere “S” para sim ou “N” para não. O programa deve emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 'Suspeito', entre 3 ou 4 como 'Cúmplice' e 5 como 'Assassino'. Caso contrário, ele será classificado como 'Inocente'.


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
    pergunta1 = input('Você telefonou para a vítima (Responda S, para sim e N, para não)? ').strip().upper()
    pergunta2 = input('Esteve no local do crime (Responda S, para sim e N, para não)? ').strip().upper()
    pergunta3 = input('Mora perto da vítima (Responda S, para sim e N, para não)? ').strip().upper()
    pergunta4 = input('Devia para a vítima (Responda S, para sim e N, para não)? ').strip().upper()
    pergunta5 = input('Já trabalhou com a vítima (Responda S, para sim e N, para não)? ').strip().upper()

    pont = pontuacao(pergunta1, pergunta2, pergunta3, pergunta4, pergunta5)
    
    print(f'Classificação: {classificacao(pont)}.')
    
if __name__ == '__main__':
    main()