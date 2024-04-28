#Informar quantos doces foram produzidos na fábrica e quantos pacotes estão disponíveis para embalar.
doces=int(input('Quantos doces foram produzidos na fábrica? ').strip())
pacotes=int(input('Quantas embalagens você possui para enrolar os doces? ').strip())

#Informar quantos doces haverá em cada pacote.
print('Para que cada pacote tenha a mesma quantidade de doces, você deve pôr', doces//pacotes, 'unidades em cada embalagem.')