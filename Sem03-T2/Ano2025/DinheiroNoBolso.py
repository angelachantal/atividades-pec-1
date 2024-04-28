#Desafio Passo 1: Calcular quanto uma pessoa ganharia se lavasse 12 carros por R$12,50. 
Total = str(12*12.5)

print("Se você lavar 12 carros por R$ 12.50, você vai receber R$"+Total)

#Calcular quanto uma pessoa ganharia lavando carros. 
print("Quantos carros você lavou?")

Carros = input()

print("Qual o valor de cada lavagem em R$?")

Valor= input()

print("Você ganhou em R$:") 
print(float(Carros)*float(Valor))