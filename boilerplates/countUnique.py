"""
Count the number of unique words in a given list
"""

def uniqueCount(lst):
    if lst:
        s = set(lst)
        return len(s)
    else:
        return 0

if __name__ == "__main__":
    print(uniqueCount([ 'one', 'two', 'two']))