import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31

        if divisor == 0:
            return MAX_INT

        neg_flag = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        power = 1
        current_divisor = divisor
        current_dividend = dividend

        while current_dividend >= current_divisor:
            current_dividend -= current_divisor
            power += 1  # double to next power of 2
            current_divisor += current_divisor  # double to next power of 2 * divisor

        quotient = 0
        while power >= 1:
            if dividend >= current_divisor: #is this power of two in our dividend?
                dividend -= current_divisor
                quotient += power
            power >>= 1  # half to next lower power of 2 using bitshift operator
            current_divisor >>= 1  # half to next lower power of 2 * divisor

        return quotient if not neg_flag else (-1)*quotient

if __name__ == "__main__":
    s = Solution()
    # assert (s.divide(7, -3)) == -2
    # assert (s.divide(10, 3)) == 3
    # assert (s.divide(10, -3)) == -3
    # assert (s.divide(1, 1)) == 1
    # assert (s.divide(-1, 1)) == -1
    # assert (s.divide(-2147483648, -1)) == 2147483647
    # assert (s.divide(2147483647, 1)) == 2147483647
    print(s.divide(10, 3))