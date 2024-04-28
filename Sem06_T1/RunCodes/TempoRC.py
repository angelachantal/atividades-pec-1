
def hh(segundos):
    return segundos//3600

def mm(segundos):
    segundos= segundos%3600
    return segundos//60

def tempo(segundos):
    ss = segundos%60
    print(f'{hh(segundos)}:{mm(segundos)}:{ss}')

def main():
    
    segundos=int(input().strip())
    tempo(segundos)

if __name__=='__main__':
    main()
