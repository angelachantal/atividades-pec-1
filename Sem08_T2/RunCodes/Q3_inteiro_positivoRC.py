def n_divisivel(n):
    if (n%3)==0 and (n%5)!=0:
        return ("FIZZ")
    elif (n%5)==0 and (n%3)!=0:
        return ("BUZZ")
    elif (n%3)==0 and (n%5)==0:
        return ("FIZZBUZZ")
    else:
        return (n)

def main():
    n = int(input('').strip())
    print(n_divisivel(n))
    if n<0:
        raise ValueError('')
if __name__=='__main__':
    main()