from assignments.Topic.StacksQueues.DoublyLinkedBase import _DoublyLinkedBase

""" Implementing double ended queue using doubly linked list """
class Deque(_DoublyLinkedBase):

    def first(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        else:
            return self._head._next._element

    def last(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        else:
            return self.tail._prev._element

    def insert_first(self, e):
        """ Insert bewteen head and first node """
        self.insert_between(e, self._head, self._head._next)

    def insert_last(self, e):
        self.insert_between(e, self._tail._prev, self._tail)

    def delete_first(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        return self.delete_node(self._head._next)

    def delete_last(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        return self.delete_node(self._tail._prev)