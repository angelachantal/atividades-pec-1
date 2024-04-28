#Preço dos ingredientes da poção mágica:
PreçoPó=5
PreçoEssência=3
PreçoLágrimas=8

#Informar a quantidade de cada ingrediente necessária para preparar a poção mágica e o custo total:
Pó=int(input('Quantas porções de Pó de Lua Estelar são necessárias para o preparo da poção mágica?').strip())
Essência = int(input('Quantas porções de Essência de Dragão são necessárias para o preparo da poção mágica?').strip())
Lágrimas = int(input('Quantas porções deLágrimas de Fênix são necessárias para o preparo da poção mágica?').strip())
print('O custo total da poção será de', PreçoPó*Pó + PreçoEssência*Essência + PreçoLágrimas*Lágrimas, 'moedas de ouro')