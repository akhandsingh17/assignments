def gcd(num1, num2):
   if num1 == 0 or  num2 == 0:
       return 0
   big = num1 if num1 > num2 else num2
   small = num1 if num1 < num2 else num2
   while big % small !=0:
       rem = big % small
       big = small
       small = rem
   return small

if __name__ == "__main__":
    assert gcd(20, 0) == 0
    assert gcd(13, 13) == 13
    assert gcd(37, 600) == 1
    assert gcd(20, 100) == 20
    assert gcd(624129, 2061517) == 18913
