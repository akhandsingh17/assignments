class ArrayStack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.isEmpty():
            raise ("empty stack")
        else:
            return self.data.pop()

def WordInverse(mystr):
    """
    reverse the input string in O(n) time
    :param mystr:
    :return:
    """
    stack = ArrayStack()
    for word in mystr.split():
        stack.push(word)
    result = ''
    while not (stack.isEmpty()):
        result = result + ' ' + stack.pop()
    return result

if __name__ == "__main__":
    mystr = 'I am using hackerrank to improve programming'
    print(WordInverse(mystr))