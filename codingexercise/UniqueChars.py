def uniquechar(str1):

    dict={}

    for i in range(0,len(str1)):
        key=str1[i]

        if key in dict.keys():
            return False
        else:
            dict[key]=1

    return True

assert(uniquechar('mary')) == True
assert(uniquechar('maryr')) == False
