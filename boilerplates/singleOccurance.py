from collections import Counter

def singleNumber(A):
    """
    Get the list of numbers with single frequency
    :param A:
    :return:
    """
    freq = dict(Counter(A))
    return list(filter(lambda x: x[1] == 1, freq.items()))[0][0]

if __name__ == "__main__":
    A=[1 ,2 ,2, 3, 1]
    print(singleNumber(A))