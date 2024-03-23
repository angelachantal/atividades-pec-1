nota1 = float(input().strip())
nota2 = float(input().strip())
nota3 = float(input().strip())

media_ponderada = (((nota1*2)+(nota2*3)+(nota3*5)))/10

print(f'{media_ponderada: .2f}')