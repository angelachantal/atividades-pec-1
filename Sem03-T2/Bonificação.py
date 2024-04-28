# Ler o tempo de serviço de um funcionário e o valor do bônus por ano trabalhado. 
tempo=float(input('Informe quantos meses você já trabalhou na Bate Ponto LTDA: ').strip())
bonus=float(input('Informe o valor do bônus para cada mês trabalhado: ').strip())

# Mostrar na tela quanto será a bonificação do funcionário.
bonificação=tempo*bonus
print(f'Parabéns! Você trabalhou {tempo:.0f} meses na Bate Ponto LTDA. Por isso, irá receber uma bonificação de R${bonificação:.2f}.')