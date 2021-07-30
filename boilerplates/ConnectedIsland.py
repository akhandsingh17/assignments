"""
Given a boolean 2D matrix, find the number of islands.
A group of connected 1s forms an island. For example, the below matrix contains 5 islands

Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1}
Output : 5

"""


class Graph(object):

    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)
        self.col = len(graph[0])

    # A safe method to check if given node (i,j) can be added to DFS
    def isSafe(self, i, j, visited):
        return ((0 <= i < self.row) and (0 <= j < self.col) and
                not visited[i][j] and self.graph[i][j])

    # A utility function to do DSF for a 2D Boolean matrix. For each cell there could be 8 possible directions.

    def DFS(self, i, j, visited):
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Mark this cell as visited
        visited[i][j] = True

        # recursion for all connected neighbours for a given cell
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)

    # Main function to that returns the count of connected islands

    def countIslands(self):
        # make a boolean array to track visited nodes and mark them False
        visited = [[False for j in range(self.col)] for i in range(self.row)]

        # loop through the matrix and count the number of times DFS is called
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                if visited[i][j] == False and self.graph[i][j] == 1:
                    self.DFS(i, j, visited)
                    count += 1
        return count


def main():
    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]
    g = Graph(graph)
    assert g.countIslands() == 5

    graph = [[1, 1, 1, 1, 0],
             [1, 1, 0, 1, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    g = Graph(graph)
    assert g.countIslands() == 1


if __name__ == '__main__':
    main()
