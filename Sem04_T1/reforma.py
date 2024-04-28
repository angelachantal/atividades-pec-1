# Reforma da sala - Variáveis: altura, comprimento e largura, em metros.

altura = float(input('Pé direito da sala (em metros): ').strip())
comprimento = float(input('Comprimento da sala (em metros): ').strip())
largura = float(input('Largura da sala (em metros): ').strip())

# Calcular a quantidade de piso para uma sala e a quantidade de tinta para as paredes, a partir das áreas. 
piso = comprimento * largura
paredes = (2 * altura * comprimento) + (2* altura * largura)

# Calcular o volume da sala em metros cúbicos para estimar a potência necessária para o ar condicionado. 
volume = altura * comprimento * largura

# Imprimir o resultado.
print(f'\n- Área do piso da sala: {piso:.2f}m².')
print(f'- Volume da sala: {volume:.2f}m³.') 
print(f'- Área das paredes da sala: {paredes:.2f}m².')