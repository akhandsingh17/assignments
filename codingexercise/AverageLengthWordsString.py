'''
Find the Average length of the word in the string.
'''

def AverageLenghtWordsString(str1):
    filtered = ''.join(filter(lambda x: x not in '".,;!', str1))
    words = [word for word in filtered.split() if word]
    avg = sum(map(len, words))/len(words)
    return "{:.2f}".format(avg)


def main():

    str1='The sky is very blue today'
    print(AverageLenghtWordsString(str1))

    str1 = 'This is another example of word length'
    print(AverageLenghtWordsString(str1))

    str1 = 'United States'
    print(AverageLenghtWordsString(str1))

if __name__=='__main__':
    main()