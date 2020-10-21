def maxTupe(lst):
    result = max(lst, key=lambda x: sum(x))
    return result

if __name__ == "__main__":
    lst=[[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
    print(maxTupe(lst))