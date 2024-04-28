#Definir quantidade de fatias de pizza.
pizza=int(input("Informe a quantidade de fatias de pizza: ").strip())

#Definir com quantas pessoas será dividida a pizza.
amigos=int(input('Com quantos amigos você quer dividir a pizza? ').strip())

#Calcular quantas fatias de pizza cada um vai receber e quantas irão sobrar.
divisão=pizza//amigos
sobra=pizza%amigos
print(f'Cada pessoa vai ganhar {divisão} fatia(s) de pizza e irá sobrar {sobra} fatia(s).')