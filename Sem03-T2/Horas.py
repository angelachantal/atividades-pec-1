#Ler uma quantidade de minutos 
Tempo=int(input('Digite o tempo em minutos: ').strip())

# Mostrar a quantidade de horas e de minutos equivalente.
horas=int(Tempo//60)
minutos=int(Tempo%60)
print(f'O tempo total foi de {horas}h{minutos}min.')