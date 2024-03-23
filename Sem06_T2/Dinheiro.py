# Nem sempre as transações financeiras resultam em números inteiros. Vamos usar o round() para resolver isso! Peça ao usuário para inserir uma quantidade de dinheiro. Em seguida, arredonde esse valor para o número inteiro mais próximo e imprima o resultado.

def inteiro(valor):
    return round(valor)

def main():
    valor=float(input('Informe o valor do dinheiro: ').strip())
    print(f'O valor arredondado é {inteiro(valor)}.')
if __name__=='__main__':
    main()