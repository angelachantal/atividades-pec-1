
def percentual(valor, porcentagem):

    return valor*(porcentagem/100)


pr=float(input('Preço: '))

vr_p=float(input('Percentual: '))

pr_acres=pr+percentual(pr,vr_p)

pr_desc=pr-percentual(pr,vr_p)

print(f'R${pr} com acréscimo de {vr_p}% fica {pr_acres}')

print(f'R${pr} com acréscimo de {vr_p}% fica {pr_desc}') 