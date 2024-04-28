# Ler valores inteiros para hora, minuto e segundo. 
# Em seguida, calcular e imprimir quantos segundos se passaram no total desde a última meia-noite até a hora lida.

hh = int(input('Hora(s): ').strip())
mm = int(input('Minuto(s): ').strip())
ss = int(input('Segundo(s): ').strip())

segundos = ss + (mm * 60) + ((hh*60)*60)

print (f'A hora atual é {hh}:{mm}:{ss}. Desde a última meia-noite (00:00:00), passaram-se {segundos} segundos.')