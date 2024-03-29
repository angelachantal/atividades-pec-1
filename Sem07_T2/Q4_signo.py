# Escreva um programa que leia a data de nascimento do usuário, e informa qual o seu signo. Considere exatamente: Áries (21/03 a 19/04); Touro (20/04 a 20/05); Gêmeos (21/05 a 21/06); Câncer (22/06 a 22/07); Leão (23/07 a 22/08); Virgem (23/08 a 22/09); Libra (23/09 a 22/10); Escorpião (23/10 a 21/11); Sagitário (22/11 a 21/12); Capricórnio (22/12 a 19/01); Aquário (20/01 a 18/02); Peixes (19/02 a 20/03)

def signo(dd, mm):
    if(dd>=20 and mm==1) or (dd<=18 and mm==2):
        return 'Aquário'
    elif (dd>=19 and mm==2) or (dd<21 and mm==3):
        return 'Peixes' 
    elif (dd>=21 and mm==3) or (dd<=19 and mm==4):
        return 'Áries'   
    elif (dd>=20 and mm==4) or (dd<=20 and mm==5):
        return 'Touro' 
    elif (dd>=21 and mm==5) or (dd<=21 and mm==6):
        return 'Gêmeos' 
    elif (dd>=22 and mm==6) or (dd<=22 and mm==7):
        return 'Câncer'
    elif (dd>=23 and mm==7) or (dd<=22 and mm==8):
        return 'Leão'
    elif (dd>=23 and mm==8) or (dd<=22 and mm==9):
        return 'Virgem'
    elif (dd>=23 and mm==9) or (dd<=22 and mm==10):
        return 'Libra'
    elif (dd>=23 and mm==10) or (dd<=21 and mm==11):
        return 'Escorpião'
    elif (dd>=22 and mm==11) or (dd<=21 and mm==12):
        return 'Sagitário'
    elif (dd>=22 and mm==12) or (dd<=19 and mm==1):
        return 'Capricórnio'

def main():
    dd = int(input('Dia: ')).strip()
    mm = int(input('Mês: ')).strip()
    print (f'Signo: {signo(dd, mm)}.')
if __name__=='__main__':
    main()