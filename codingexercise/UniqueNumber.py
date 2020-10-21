def UniqueNumber(n):
    dict = {}
    key=0
    while(n!=0):
        key=n%10
        if key in dict.keys():
            return False
        else:
            dict[key]=1
            n=int(n/10)
    return True

def main():
    # Driver program
    n = 321
    print UniqueNumber(n)

if __name__=='__main__':
    main()


