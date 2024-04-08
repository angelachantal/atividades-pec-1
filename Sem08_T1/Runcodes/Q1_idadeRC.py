def idade(hoje, nascimento):
    anos = hoje - nascimento
    return (anos)

def main():
    d_hoje = int(input().strip())
    m_hoje = int(input().strip())
    a_hoje = int(input().strip())
    
    d_nascimento = int(input().strip())
    m_nascimento = int(input().strip())
    a_nascimento = int(input().strip())
    
    anos = int(idade(a_hoje, a_nascimento))
    
    if m_hoje < m_nascimento: 
        print (anos - 1)
    elif m_hoje == m_nascimento and d_hoje < d_nascimento:
        print (anos - 1)
    else:
        print (anos)
if __name__=='__main__':
    main()