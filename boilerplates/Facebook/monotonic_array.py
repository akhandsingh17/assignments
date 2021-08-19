## Given an array of integers, we would like to determine whether the array is monotonic

def isMonotonic(arr):
    return (
            all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) or
            all(arr[i] >= arr[i+1] for i in range(len(arr)-1))
    )


if __name__ == "__main__":
    assert (isMonotonic([1, 2, 5, 5, 8])) == True
    assert (isMonotonic([9, 4, 4, 2, 2])) == True
    assert (isMonotonic([1, 4, 6, 3])) == False
    assert (isMonotonic([1, 1, 1, 1, 1])) == True