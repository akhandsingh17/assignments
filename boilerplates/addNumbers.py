"""
 Given a two digit number, return the sum of the numbers. Otherwise return the number itself.
"""

def addingNumber(num):
    temp = num
    sum = 0
    try:
        if num > 9:
            while temp != 0:
                sum += (temp % 10)
                temp = int(temp/10)
            return sum
        else:
            return num
    except:
        return 0

if __name__ == "__main__":
    assert addingNumber(38) == 11
    assert addingNumber(11) == 2
    assert addingNumber(5) == 5
    assert addingNumber(1234) == 10
    assert addingNumber('') == 0


