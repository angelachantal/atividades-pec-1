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
    dd = int(input())
    mm = int(input())
    print (f'{signo(dd, mm)}')
if __name__=='__main__':
    main()