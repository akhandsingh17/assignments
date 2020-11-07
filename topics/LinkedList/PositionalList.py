from assignments.Topic.StacksQueues.DoublyLinkedBase import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """ A sequential container of elemtns allowing positional access """

    class Position:
        """ An abstraction representing a location of a single element """
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            """ Return True if other is a position representing the same node """
            return type(other) is type(self) and self._node is other._node

        def __ne__(self, other):
            """ Return True if other is a position does not represent the same node """
            return not (self == other)

        def __str__(self):
            return 'Node <{}>'.format(self._node)

    # --- Utility Methods -----

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position Type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node


    def _make_position(self, node):
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position(self, node)   # valid position

    # --- Accessor Methods -----

    def first(self):
        return self._make_position(self._head._next)

    def last(self):
        return self._make_position(self._tail._prev)

    def before(self,p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self,p):
        node = self._validate(p)
        return self._make_position(node._next)

    def iter(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # --- Mutator Methods -----
    # -- override inherited version to return position instead of node

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._head, self._head._next)

    def add_last(self, e):
        return self._insert_between(e, self._tail._prev, self._tail)

    def add_before(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def delete(self, p):
        """ Remove and return node at position p """
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        node = self._validate(p)
        old_value = node._element
        node._element = e
        return old_value

if __name__ == "__main__":
    list = PositionalList()
    list.add_last(8)
    list.add_after(list.first(), 5)
    list.add_first(9)
    list.delete(list.last())
    print(list)




