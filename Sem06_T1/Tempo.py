#Escreva um programa que leia o tempo de duração de um evento em uma fábrica expresso em segundos. Calcule e exiba esse tempo em horas, minutos e segundos (HH:MM:SS).

def hh(segundos):
    return segundos//3600

def mm(segundos):
    segundos= segundos%3600
    return segundos//60

def tempo(segundos):
    ss = segundos%60
    print(f'A duração do evento foi de {hh(segundos)}:{mm(segundos)}:{ss}')

def main():
    
    segundos=int(input('Quantos segundos durou o evento? ').strip())
    tempo(segundos)

if __name__=='__main__':
    main()

