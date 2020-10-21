def stringStruct(str):
    words = str.split()
    return ' '.join(words)


def main():

    str = '       I work          in Amazon in Seattle       I           life         '
    print stringStruct(str)

if __name__=='__main__':
    main()

