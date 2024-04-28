#Ler o valor de um produto, a partir do teclado, e guardar na variável "preço", convertida para real.vars
preco = float(input('Informe o preço do produto: ').strip())
#Calcular o valor do produto com desconto de 10% e mostrar o resultado na tela.
desconto=(preco*0.1)
PrecoFinal=(preco-desconto)
print(f'O valor do produto com 10% de desconto é R$ {PrecoFinal:.2f}')