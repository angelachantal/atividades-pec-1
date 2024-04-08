#Escreva um programa que leia um número inteiro positivo e escreva na tela:
#FIZZ se o número é divisível por três;
# para cada número lido apenas uma resposta deve ser impressa.
def n_divisivel(n):
    if (n%3)==0 and (n%5)!=0:
        return ("FIZZ")
    elif (n%5)==0 and (n%3)!=0:
        return ("BUZZ")
    elif (n%3)==0 and (n%5)==0:
        return ("FIZZBUZZ")
    else:
        return (n)

def main():
    n = int(input('Digite um número inteiro positivo: ').strip())
    print(n_divisivel(n))
    if n<0:
        raise ValueError('O número deve ser maior que 0.')
if __name__=='__main__':
    main()