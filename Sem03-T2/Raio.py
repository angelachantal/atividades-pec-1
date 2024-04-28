# Ler o valor inserido pelo teclado e guardar na variável raio, convertido para real.
raio = float(input('Digite o valor do raio: ').strip())
# Calcular o valor da circunferência para o raio lido e mostrar o resultado na tela.
circunferencia = (2*3.141592*raio)
print(f'O valor da circunferência para esse raio é {circunferencia:.6f}')
# Calcular a área do círculo para o raio lido e mostrar o resultado na tela.
circulo = (3.141592*raio**2)
print(f'A área do círculo para esse raio é {circulo:.6f}')
# Calcular a área da esfera para o raio lido e mostrar o resultado na tela.
esfera = (4*3.141592*raio**2)
print(f'A área da superfície da esfera para esse raio é {esfera:.6f}')
# Calcular o volume da esfera para o raio lido e mostrar o resultado na tela.
volume = ((4/3)*3.141592*raio**3)
print(f'O volume da esfera para esse raio é {volume:.6f}')