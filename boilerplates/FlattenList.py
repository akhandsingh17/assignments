
def FlattenList(lst):
    """
    Input list is a combination of list of tuples and list of lists.
    :param lst:
    :return: flattened list
    """
    result = []
    for i in lst:
        if isinstance(i,(list,tuple)):
            result.extend(FlattenList(i))
        else:
            result.append(i)
    return result

if __name__ == "__main__":
    lst=[1,2,[1,2,3,[3,3],(5,6,7)],4,5,6,[7,6,4],[8,7,4,5,[6,7,8]]]
    print(FlattenList(lst))