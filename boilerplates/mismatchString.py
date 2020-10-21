# For example:
#           - string 1 : "Firstly this is the first string"
#           - string 2 : "Next is the second string"
#           - output : ['Firstly', 'this', 'first', 'Next', 'second']

def return_mismatched(str1, str2):
    if str1 == "" and str2 == "":
        return []
    if str1 == "":
            return [word for word in str2.split()]
    if str2 == "":
        return [word for word in str1.split()]
    result = []
    set1 = set([word for word in str1.split()])
    set2 = set([word for word in str2.split()])
    for words in set1.difference(set2):
        result.append(words)
    for words in set2.difference(set1):
        result.append(words)
    return result

def cmp_lst(l1,l2):
    return sorted(l1) == sorted(l2)

assert cmp_lst(return_mismatched("",""), []) == True
assert cmp_lst(return_mismatched("","This is the second string"), ['This','is','the','second','string']) == True
assert cmp_lst(return_mismatched("This is the first string",""), ['This','is','the','first','string']) == True
assert cmp_lst(return_mismatched("This is the first string","This is the second string"),['first', 'second']) == True
assert cmp_lst(return_mismatched("This is the first string extra","This is the second string"),['first', 'second', 'extra']) == True
assert cmp_lst(return_mismatched("This is the first text","This is the second string"),['first', 'text', 'second', 'string']) == True
assert cmp_lst(return_mismatched("Firstly this is the first string","Next is the second string"), ['Firstly', 'this', 'first', 'Next', 'second']) == True
print('passed')