# Um alienígena chamado Zob precisa de ajuda para converter anos terrestres em anos espaciais! Sabendo que 1 ano terrestre equivale a meio ano espacial, calcule e imprima uma idade inserida pelo usuário em anos espaciais.

def anos_espaciais(anos_terrestres):
    return round(anos_terrestres*0.5)

def main():
    anos_terrestres = int(input('Qual a idade de Zob na Terra? ').strip())
    print(f'Zob tem {anos_espaciais(anos_terrestres)} anos espaciais.')
if __name__=='__main__':
    main()