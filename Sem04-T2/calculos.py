#Escrevr um programa que leia dois valores e mostre na tela, nessa ordem: a soma dos números; aconcatenação das strings; a multiplicação dos números;
# a multiplicação como strings; a divisão dos números; a divisão inteira dos números; a exponenciação; e 0 módulo (resto).

n1 = float(input('Informe o primeiro número: ').strip())
n2 = int(input('Informe o segundo número: ').strip())

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


print(f'Soma: {soma}')
print(f'Concatenação: {concatenacao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Multiplicação como string: {multiplicacao_str}')
print(f'Divisão: {divisao}')
print(f'Divisão inteira: {divisao_inteira}')
print(f'Exponenciação: {exponenciacao}')
print(f'Módulo (resto): {modulo}')
