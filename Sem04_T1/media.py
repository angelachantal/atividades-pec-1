# Ler três números inteiros nas variáveis “a”, “b” e “c” e escrever a média entre eles: (a + b + c) / 3.

a = int(input('Informe o primeiro número: ').strip())

b = int(input('Informe o segundo número: ').strip())

c = int(input('Informe o terceiro número: ').strip())

media = (a + b + c)/3
media = str(media)

print (f'A média entre os números é {media}.')