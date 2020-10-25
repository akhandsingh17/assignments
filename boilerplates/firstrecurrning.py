def firstrecurring(mystr):
    dct = {}
    for chr in mystr:
        if chr in dct.keys():
            return chr
        else:
            dct[chr] = 1

if __name__ == "__main__":
    mystr = 'akhans'
    print(firstrecurring(mystr))
