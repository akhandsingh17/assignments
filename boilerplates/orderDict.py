from collections import defaultdict

def orderDcit(lst):
    dd = defaultdict(list)
    for k, v in lst:
        dd[k].append(v)
    return dd

if __name__ == "__main__":
    st = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
    print(orderDcit(st))