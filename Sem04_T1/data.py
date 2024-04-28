# As variáveis “dia”, “mês” e “ano” contêm os valores respectivos de uma data. 
# Escrever um comando “print” que imprima essa data no formato usado, por exemplo, “15/4/2020” ou “2/12/2004”.

dd = int(input('Dia: ').strip())
dd = str(dd)

mm = int(input('Mês: ').strip())
mm = str(mm)

aaaa = int(input('Ano: ').strip())
aaaa = str(aaaa)

print('DATA: ' + dd + '/' + mm + '/' + aaaa )