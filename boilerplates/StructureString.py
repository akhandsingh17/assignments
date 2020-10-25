def StructureString(mystr):
    lst = [word for word in mystr.split()]
    return ' '.join(lst)

if __name__ == "__main__":
    mystr = '       I work          in Amazon in Seattle            life         '
    print(StructureString(mystr))