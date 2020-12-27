"""
Reverse a string using recursion

"""

def reverseString(s):
    """
    :type s: List[str]
    :rtype: void Do not return anything, modify s in-place instead.
    """
    n = list(s)
    def helper(start, end, ls):
        if start >= end:
            return

        # swap the first and last element
        ls[start], ls[end] = ls[end], ls[start]
        return helper(start+1, end-1, ls)

    helper(0, len(s)-1, n)
    return n

if __name__ == "__main__":
    print(reverseString('akhans'))