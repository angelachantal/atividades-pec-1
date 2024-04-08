# Nesta versão, fiz a separação da data, a exemplo do que foi apresentado na atividade "Quebra-Cabeça". 
# A versão 2 apresenta o código como foi inserido no Runcodes.

def idade(hoje, nascimento):
    a_atual = hoje % 10000
    hoje //= 10000
    m_atual = hoje % 100
    hoje //= 100
    d_atual = hoje
    
    a_nasc = nascimento % 10000
    nascimento //= 10000
    m_nasc = nascimento % 100
    nascimento //= 100
    d_nasc = nascimento
    
    anos = a_atual - a_nasc
    meses = m_atual - m_nasc
    dias = d_atual - d_nasc
    return (f'Idade: {anos} anos, {meses} meses e {dias} dias')

def main():
    hoje = int(input('Data atual (formato DDMMAA): \n').strip())
    nascimento = int(input('Data de nascimento (formato DDMMAA): \n').strip())
    
    print(idade(hoje, nascimento))
if __name__=='__main__':
    main()