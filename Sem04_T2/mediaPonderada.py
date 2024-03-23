# Escrever um programa que leia três notas de um aluno, depois calcule e escreva a média ponderada deste aluno, considerando que o peso das notas são 2, 3 e 5. 
# Fórmula para o cálculo da média final é: média ponderada = ((n1 ∗ 2) + (n2 ∗ 3) + (n3 ∗ 5))/10

nota1 = float(input('Nota 1: ').strip())
nota2 = float(input('Nota 2: ').strip())
nota3 = float(input('Nota 3: ').strip())

media_ponderada = (((nota1*2)+(nota2*3)+(nota3*5)))/10

print(f'Média: {media_ponderada: .2f}')