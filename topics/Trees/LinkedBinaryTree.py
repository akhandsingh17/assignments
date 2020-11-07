class Tree:
    """ Abstract base class representing the Tree"""
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not (self == other)

    """ Abstract methods for concrete subclass """
    def root(self):
        """ Return position representing root otherwise None"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """ Return position representing p's parent other None if p is root """
        NotImplementedError('must be implemented by subclass')

    def num_children(self, p ):
        """ Number of children that position P has """
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """ generate an iteration of position for p's children """
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    """" concrete methods in the class """
    def is_empty(self):
        return len(self) == 0

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def depth(self, p):
        if self.is_leaf(p) == 0 :
            return 0
        else:
            return 1  + (self.depth(self.parent(p)))

    def height(self, p):
        if self.is_root(p) == 0:
            return 0
        else:
            return 1 + max( self.height(c) for c in self.children(p))


class BinaryTree(Tree):
    """ Abstract base class representing a binary tree structure """

    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """ Return a position representing p's right child  """
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p ):
        """ Return the position representing left of right child of  p """
        parent = self.parent(p)
        if parent is None:
            return None   # p must be root
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """ Generate an iteration of position representing p's children """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

class LinkedBinaryTree(BinaryTree):
    """ Linked representation of binary tree """
    class _Node:  # Lightweight non-public class for storing a node
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container , node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if isinstance(p, self.Position):
            raise TypeError('p must be proper position type')
        if p._node._parent is p._node :
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(node) if node is not None else None

    def add_root(self, e):
        if self.root() is not None:
            raise ValueError('Root Exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child already exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child already exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

