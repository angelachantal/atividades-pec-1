# Escrever um programa que leia a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho) e retorne as respectivas mensagens “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.

def semaforo(cor):
    if cor == "V":
        return "Siga"
    elif cor == "A":
        return "Atenção"
    elif cor == "E":
        return "Pare"
def main():
    cor = input('Cor do semáforo (V = verde; A = amarelo; E = vermelho): ').upper()
    print(f'{semaforo(cor)}')
if __name__=='__main__':
    main()