"""
You have a 2-D array of friends like [[A,B],[A,C],[B,D],[B,C],[R,M], [S],[P], [A]]
Write a function that creates a dictionary of how many friends each person has.
People can have 0 to many friends. However, there won't be repeat
relationships like [A,B] and [B,A] and neither will there be more than 2 people in a relationship
"""
from collections import defaultdict

def facebookfriends(matrix):
    dct = defaultdict(list)
    for rel in matrix:
        for p in rel:
            if len(rel) > 1:
                dct[p].extend(list( x for x in rel if x not in p))
            else:
                dct[p].append('')
    result = {k: sum(map(len, v)) for k, v in dct.items()}
    return result


if __name__ == "__main__":
    matrix = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'C'], ['R', 'M'], ['S'], ['P'], ['A']]
    print(facebookfriends(matrix))
