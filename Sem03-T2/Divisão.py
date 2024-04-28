#Ler dois valores, um dividendo e um divisor. 
dividendo = float(input('Informe o valor do dividendo: ').strip())
divisor = float(input('Informe o valor do divisor: ').strip())

#Mostrar o resultado da divisão e o resto da divisão inteira dos valores.
quociente = float(dividendo//divisor)
resto = float(dividendo%divisor)
print(f'O resultado da divisão interira é {quociente: 0.4f} e o resto é {resto: 0.4f}.')
