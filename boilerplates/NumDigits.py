"""
Write a function that takes a number and returns a list of
its digits
"""
def solution(num):
    result = []
    while num != 0:
        carry = num % 10
        num = num // 10
        result.append(carry)
    result.reverse()
    return result

if __name__ == "__main__":
    assert solution(123) == [1, 2, 3]
    assert solution(400) == [4, 0, 0]