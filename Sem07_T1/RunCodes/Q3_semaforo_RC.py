def semaforo(cor):
    if cor == "V":
        return "Siga"
    elif cor == "A":
        return "Atenção"
    elif cor == "E":
        return "Pare"
def main():
    cor = input().upper()
    print(f'{semaforo(cor)}')
if __name__=='__main__':
    main()