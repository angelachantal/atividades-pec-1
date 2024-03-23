def anos_espaciais(anos_terrestres):
    return int(anos_terrestres*0.5)

def main():
    anos_terrestres = int(input().strip())
    print(f'{anos_espaciais(anos_terrestres)}')
if __name__=='__main__':
    main()