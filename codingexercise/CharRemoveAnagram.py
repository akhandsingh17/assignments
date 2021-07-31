# Given two strings in lowercase, the task is to make them Anagram. The only allowed operation is to remove a
# character from any string. Find minimum number of characters to be deleted to make both the strings anagram? If two
# strings contains same data set in any order then strings are called Anagrams.

def CharRemoveAnagram(s1, s2):
    big = s1 if len(s1) > len(s2) else s2
    small = s1 if len(s1) < len(s2) else s2
    map1 , map2 = {}, {}
    for c in big:
        map1[c] = map1.get(c, 0) + 1
    for c in small:
        map2[c] = map2.get(c, 0) + 1
    for k, v in map1.items():
        if k in map2.keys():
            map1[k] = map1.get(k, 0) - 1

    return len(list(filter(lambda x:x[1] == 1 , map1.items())))

def main():
    assert CharRemoveAnagram(s1='bcadeh', s2='hea') == 3
    assert CharRemoveAnagram(s1='cddgk', s2='gcd') == 2
    assert CharRemoveAnagram(s1='bca', s2='acb') == 0


if __name__ == '__main__':
    main()
