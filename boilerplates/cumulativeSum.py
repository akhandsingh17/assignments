"""
Write a function that returns the cumulative sum of
elements in a list
"""

def solution(input):
    result = []
    key = 0
    for i in input:
        key += i
        result.append(key)
    return result

if __name__ == "__main__":
    assert solution([1, 1, 1]) == [1, 2, 3]
    assert solution([1, -1, 3]) == [1, 0, 3]