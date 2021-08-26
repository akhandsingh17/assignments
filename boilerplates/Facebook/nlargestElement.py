# Given a ´dictionary, print the key for nth highest value present in the dict.
# If there are more than 1 record present for nth highest value then sort the key and
# print the first one.


input = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 3, 'f': 4, 'g': 5}


def nHighestVal(input, k):
    input = sorted(input.items(), key=lambda x: x[1], reverse=True)
    return input[k-1]

print(nHighestVal(input, 3))