# Camel case of a given sentence Given a sentence, task is to remove spaces from the sentence and rewrite in Camel
# case. It is a style of writing where we don’t have spaces and all words begin with capital letters.


def CamelCaseSentence(s):
    words = [word.title() for word in s.split() if word]
    return ''.join(words)

def main():
    assert CamelCaseSentence('I got intern at geeksforgeeks') == 'IGotInternAtGeeksforgeeks'
    assert CamelCaseSentence('Here comes the garden') == 'HereComesTheGarden'

if __name__ == '__main__':
    main()
