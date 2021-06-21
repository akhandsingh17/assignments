import collections

def most_common(ary):
    freq = collections.Counter(ary).most_common()
    result = list(filter(lambda x:x[1] > 1, freq))
    return result
if __name__ == "__main__":
    ary = [4, 8, 4, 7, 8, 8, 5, 2, 7, 7, 7, 7, 3, 2, 1, 1]
    print(most_common(ary))