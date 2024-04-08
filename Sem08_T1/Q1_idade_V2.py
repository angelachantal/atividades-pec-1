def idade(hoje, nascimento):
    anos = hoje - nascimento
    return (anos)

def main():
    d_hoje = int(input('Dia atual: ').strip())
    m_hoje = int(input('Mês atual: ').strip())
    a_hoje = int(input('Ano Atual: ').strip())
    
    d_nascimento = int(input('Dia de Nascimento: ').strip())
    m_nascimento = int(input('Mês de Nascimento: ').strip())
    a_nascimento = int(input('Ano de Nascimento: ').strip())
    
    anos = int(idade(a_hoje, a_nascimento))
    
    if m_hoje < m_nascimento: 
        print (f'Idade: {anos - 1}')
    elif m_hoje == m_nascimento and d_hoje < d_nascimento:
        print (f'Idade: {anos - 1}')
    else:
        print (f'Idade: {anos} anos')
if __name__=='__main__':
    main()