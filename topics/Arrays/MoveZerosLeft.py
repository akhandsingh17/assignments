"""
Given an array nums, write a function to move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

"""

def move_zeros(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
            k = i
            while k < len(arr)-1:
                arr[k] = arr[k+1]
                k += 1
            arr[-1] = 0
        else:
            continue
    return arr


if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    print(move_zeros(arr))
