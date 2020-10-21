"""
Trie is a very useful data structure. It is commonly used to represent a dictionary for looking up words in a vocabulary.
For example, consider the task of implementing a search bar with auto-completion or query suggestion.
When the user enters a query, the search bar will automatically suggests common queries starting with the characters
input by the user.
"""


class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        self.children = {}
        self.counter = 0
        self.is_last = False
        self.char = char


class Trie:
    def __init__(self):
        """ The trie has at least the root node. The root node does not store any character"""
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        # Mark the end of a word
        node.is_last = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def dfs(self, node, prefix):
        """ Depth-first traversal of the trie """
        if node.is_last:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        """ Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted """

        self.output = []
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.dfs(node, x[:-1])

        return sorted(self.output, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    t = Trie()
    t.insert("was")
    t.insert("word")
    t.insert("war")
    t.insert("where")
    t.insert("what")
    print(t.query("wh"))



