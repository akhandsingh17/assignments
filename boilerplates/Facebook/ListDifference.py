#Given two sentences, you have to print the words those are not present in either of the sentences


def list_difference(A, B):
    lst1 = [ word for word in A.split() if word ]
    lst2 = [ word for word in B.split() if word ]
    count = {}
    result = []
    big = lst1 if len(lst1) >= len(lst2) else lst2
    small = lst1 if len(lst1) < len(lst2) else lst2
    for word in big:
        if word in count.keys():
            count[word] = count[word] + 1
        else:
            count[word] = 1

    for word in small:
        if word in count.keys():
            count[word] = count[word] - 1
        else:
            result.append(word)
    for key , value  in count.items():
        if value > 0 :
            result.append(key)

    return result

def cmp_lst(l1,l2):
    return sorted(l1) == sorted(l2)

assert cmp_lst(list_difference("",""), []) == True
assert cmp_lst(list_difference("","This is the second string"), ['This','is','the','second','string']) == True
assert cmp_lst(list_difference("This is the first string",""), ['This','is','the','first','string']) == True
assert cmp_lst(list_difference("This is the first string","This is the second string"),['first', 'second']) == True
assert cmp_lst(list_difference("This is the first string extra","This is the second string"),['first', 'second', 'extra']) == True
assert cmp_lst(list_difference("This is the first text","This is the second string"),['first', 'text', 'second', 'string']) == True
assert cmp_lst(list_difference("Firstly this is the first string","Next is the second string"), ['Firstly', 'this', 'first', 'Next', 'second']) == True
