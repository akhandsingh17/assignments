from collections import Counter
def isMatch(str1):
    arr1=['cat', 'bat', 'rat', 'drat', 'dart', 'drab']
    arr_hash = {i:len(i) for i in arr1}
    arr_len =set(arr_hash.values())
    if len(str1) not in arr_len: return False
    if str1 in arr_hash : return True
    match_arr = [x for x in arr_hash.keys() if arr_hash[x]==len(str1)]
    found=False
    for i in range(len(str1)):
        if str1[i]==".":
            found=True
        else:
            found=False
        for j in range(len(match_arr)):
            if match_arr[j][i]==str1[i]:
                found=True
        if found==False:
            return False
    return found

assert isMatch('cat')==True
assert isMatch('c.t')==True
assert isMatch('l.t')==False
assert isMatch('.at')==True
assert isMatch('..t')==True
assert isMatch('..k')==False
assert isMatch('d..t')==True
assert isMatch('dr..')==True
assert isMatch('...')==True
assert isMatch('....')==True
assert isMatch('.....')==False