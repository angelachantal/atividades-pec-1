def maca(prc_maca, qtd=3):
    return prc_maca*qtd

def banana(prc_banana, qtd=2):
    return prc_banana*qtd

def main():
    
    prc_maca=float(input().strip())
    prc_banana=float(input().strip())
    total = maca(prc_maca)+banana(prc_banana)
    print(f'{total:.2f}')
    
if __name__=='__main__':
    main()
