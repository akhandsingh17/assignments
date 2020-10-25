def nestedSort(lst):
    """
    Sort the input list of dictionaries based on the value of the sub-key
    :param lst:
    :return:
    """
    return sorted(lst, key=lambda x: x['key']['subkey'], reverse=True)

if __name__ == "__main__":
    lst=[
        {'key': {'subkey': 1}},
        {'key': {'subkey': 10}},
        {'key': {'subkey': 5}}
    ]
    print(nestedSort(lst))