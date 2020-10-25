def largest(arr):
    if arr:
        result = int(arr[0])
        for i in range(1, len(arr)):
            if int(arr[i]) >= result:
                result = arr[i]
            else:
                continue
        return result
    else:
        return None

if __name__ == "__main__":
    assert largest([]) == None
    assert largest([10, 324, 45, 90, 9808]) == 9808
    assert largest([-5, 89, 20, 64, 20, 45]) == 89
