class ArrayStack:
    def __init__(self):
        self._slist = []

    def isEmpty(self):
        return len(self._slist) == 0

    def top(self):
        if self.isEmpty():
            raise("Stack is Empty")
        else:
            return self._slist[-1]

    def push(self,item):
        self.item = item
        if self.item:
            self._slist.append(item)

    def pop(self):
        if self.isEmpty():
            raise("Stack is Empty")
        else:
            return self._slist.pop()

    def check_balanced_string(self, in_str):
        left = ['[','(','{','<']
        right = [']',')','}','>']
        for chr in in_str:
            if chr in left:
                self.push(chr)
            elif chr in right:
                if self.isEmpty():
                    return False
                if right.index(chr) != left.index(self.pop()):
                    return False
        return self.isEmpty()

if __name__ == "__main__":
    s = ArrayStack()
    mystr = '({}[])'
    assert(s.check_balanced_string(mystr)) == True