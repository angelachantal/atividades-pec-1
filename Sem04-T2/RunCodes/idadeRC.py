anos = int(input().strip())
meses = int(input().strip())
dias = int(input().strip())

dias_totais = dias + (anos*365) + (meses*30)

print(f'{dias_totais}')