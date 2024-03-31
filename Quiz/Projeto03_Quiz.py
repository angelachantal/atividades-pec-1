#Passo 1 - Quiz com uma pergunta que mostra na tela uma carinha sorridente, caso o jogador escolher a alternativa correta.

        # print ('No Python, como se chama uma "caixa" usada para armazenar dados?')
        # resposta = input().upper()

        # if resposta == "VARIÁVEL":
        #     print(":)"* 100)
        # else:
        #     print(":(" * 100)
        #     
        # print ("Obrigada por jogar!")

#Passo 2 - Testar o código convertendo as letras da resposta para maiúscula ou para minúscula.

#Passo 3 - Quiz de múltipla escolha.

        # print ('''
        # Q1 - No Python, como se chama uma "caixa" usada para armazenar dados?
        # a) texto
        # b) variável
        # c) uma caixa de sapatos
        # ''')
        # resposta = input().lower()

        # if resposta == 'a':
        #     print (' Não - texto é um tipo de dado :(')
        # elif resposta == 'b':
        #     print (' Correto! :)')
        # elif resposta == 'c':
        #     print (' Não seja bobinho! :(')
        # else:
        #     print (' Você não escolheu a, b, nem d :(')
        
# DESAFIO - Meu Quiz (perguntas e respostas retiradas do site https://www.todamateria.com.br/perguntas-e-respostas-de-conhecimentos-gerais/)

def q1_sangue_corpo (resposta1):
    if resposta1 == 'b':
        score = 1
    else:
        score = 0
    return int(score)

def q2_doacao_sangue (resposta2):
    if resposta2 == 'b':
        score = 1
    else:
        score = 0
    return int(score)

def q3_penso_existo (resposta3):
    if resposta3 == 'c':
        score = 1
    else:
        score = 0
    return int(score)

def q4_chuveito_eletrico (resposta4):
    if resposta4 == 'c':
        score = 1
    else:
        score = 0
    return int(score) 

def q5_menor_maior_pais (resposta5):
    if resposta5 == 'a':
        score = 1
    else:
        score = 0
    return int(score) 

def main():
    print('''
    QUIZ - Conhecimentos Gerais
    \n1. Normalmente, quantos litros de sangue uma pessoa tem? 
    a) Tem entre 2 a 4 litros.
    b) Tem entre 4 a 6 litros.
    c) Tem 10 litros.
    d) Tem 7 litros.
    e) Tem 0,5 litros.
    ''')
    
    resposta1 = input().lower()
    
    if resposta1 == 'b':
        print('Correto!')
    else:
        print ('Errado!')
    
    print('''
    \n2. Em média, quantos litros de sangue são retirados numa doação de sangue?
    a) São retirados 450 mililitros
    b) São retirados 450 mililitros
    c) São retirados 2 litros
    d) São retirados 1,5 litros
    e) São retirados 0,5 litros
    ''')
    
    resposta2 = input().lower()
    
    if resposta2 == 'b':
        print('Correto!')
    else:
        print ('Errado!')
        
    print('''
    \n3. De quem é a famosa frase “Penso, logo existo”?
    a) Platão
    b) Galileu Galilei
    c) Descartes
    d) Sócrates
    e) Francis Bacon   
    ''')

    resposta3 = input().lower()
    
    if resposta3 == 'c':
        print('Correto!')
    else:
        print ('Errado!')
    
    print('''
    \n4. De onde é a invenção do chuveiro elétrico?
    a) França
    b) Inglaterra
    c) Brasil
    d) Austrália
    e) Itália
    ''')
    resposta4 = input().lower()
    
    if resposta4 == 'c':
        print('Correto!')
    else:
        print ('Errado!')

    print('''
    \n5. Quais o menor e o maior país do mundo?
    a) Vaticano e Rússia
    b) Nauru e China
    c) Mônaco e Canadá
    d) Malta e Estados Unidos
    e) São Marino e Índia    
    ''')

    resposta5 = input().lower()
    
    if resposta5 == 'a':
        print('Correto!')
    else:
        print ('Errado!')

    score = q1_sangue_corpo(resposta1) + q2_doacao_sangue (resposta2)+ q3_penso_existo (resposta3) + q4_chuveito_eletrico (resposta4)+ q5_menor_maior_pais(resposta5)
    
    if score == 5:
        print ('\n\nParabéns! Você acertou todas as questões!\n\n')
    else:
        print(f'\n\nSua pontuação foi {score}. Tente novamente!\n\n')
if __name__=='__main__':
    main()