#Definir a ditância até um planeta e a velocidade da nave:
distância = int(input('Qual a distância, em km, a ser percorrida até o planeta? ').strip())
velocidade = int(input('Qual a velocidade que a sua nave pode atingir em km/h? ').strip())

#Calcular quantos dias e quantas horas a viagem levará, considerando que um dia tem 24h.
tempo=distância//velocidade
print('Você levará', tempo//24, 'dia(s)', 'e', tempo%24, 'hora(s) para chegar ao planeta nessa nave.')