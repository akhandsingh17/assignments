
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

if __name__ == "__main__":
    s = ArrayStack()
    s.push(10)
    s.pop()
    print(s.top())

