# Print characters and their frequencies in order of occurrence Given a string str containing only lowercase
# characters. The problem is to print the characters along with their frequency in order of their occurrence and in
# the given format explained in the examples below.

from collections import OrderedDict

def CharactersFrequencyOrderOccurence(s):
    od = OrderedDict()
    for char in s:
        if char in od.keys():
            od[char] = od.get(char) + 1
        else:
            od[char] =1
    return ''.join([key + str(value) for key, value in od.items()])

def main():
    print(CharactersFrequencyOrderOccurence(s='geeksforgeeks'))
    print(CharactersFrequencyOrderOccurence(s='elephant'))


if __name__=='__main__':
    main()