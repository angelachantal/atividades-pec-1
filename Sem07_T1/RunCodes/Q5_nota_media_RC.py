def med(n1, n2, n3):
    media = (n1+n2+n3)/3
    if n3 > 8:
        return media + 1
    else:
        return media
def med_final(media):
    if media>10:
        return 10
    else:
        return media
def main():
    n1 = float(input().strip())
    n2 = float(input().strip())
    n3 = float(input().strip())
    media= med(n1,n2,n3)
    print (f'{med_final(media)}')
if __name__=='__main__':
    main()