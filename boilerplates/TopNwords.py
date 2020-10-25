from collections import Counter

def Top5Words(path):
    """
    Identify top 5 words based on their frequency from a text file.
    :param path:
    :return:
    """
    file = open(path, 'r')
    data = file.read()
    words = data.split(r'\s', data)
    lst = [word for word in words]
    count = Counter(lst)
    return count.most_common(5)

if __name__ == "__main__":
    path = '/Documents/hamlet.txt'
    print(Top5Words(path))