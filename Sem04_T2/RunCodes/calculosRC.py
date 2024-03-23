n1 = float(input().strip())
n2 = int(input().strip())

soma=n1+n2
multiplicacao = n1*n2
divisao = n1/n2
divisao_inteira = n1//n2
exponenciacao = n1**n2
modulo = n1%n2

n1=str(n1)
multiplicacao_str = n1 * n2

n2=str(n2)
concatenacao= n1 + n2


print(f'{soma}')
print(f'{concatenacao}')
print(f'{multiplicacao}')
print(f'{multiplicacao_str}')
print(f'{divisao}')
print(f'{divisao_inteira}')
print(f'{exponenciacao}')
print(f'{modulo}')