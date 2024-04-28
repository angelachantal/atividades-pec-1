#Executar um programa em Python para mostrar quantos anos uma pessoa terá em 2025, utilizando três variáveis.
print ("Em que ano você nasceu?")
nascimento = input()
nascimento = int(nascimento)
print("Para qual ano você quer saber sua idade?")
ano = input()
ano = int(ano)
idadeEm2025 = ano - nascimento
print ("Em", ano, "você terá", idadeEm2025, "anos!")