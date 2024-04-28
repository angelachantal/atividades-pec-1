distância = int(input().strip())
velocidade = int(input().strip())
tempo=distância//velocidade
print(tempo//24, 'dias e', tempo%24, 'horas')