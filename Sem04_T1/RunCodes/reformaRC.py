altura = int(input().strip())
comprimento = int(input().strip())
largura = int(input().strip)
piso = comprimento * largura
paredes = (2 * altura * comprimento) + (2* altura * largura)
volume = altura * comprimento * largura
print(f'{piso}\n{volume}\n{paredes}')