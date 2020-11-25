"""
# Input: Example data coming in line-by-line
San Francisco     100
San Francisco     200
San Francisco     150
... (more San Francisco)
New York          250
New York          110
New York          190
... (more New York)
Boston            160
Boston            100
Boston            90
... (more Boston)
... (even more markets)
<EOF>


# Output:
San Francisco     145
New York          190
Boston            160

"""

from collections import defaultdict
class Solution:
    def median_price(self, arr):
        dct = defaultdict(list)
        for item in arr:
            dct[item[0]].append(item[1])

        for market, pricelist in dct.items():
            pricelist.sort()
            if len(pricelist) % 2 != 0:
                mid = len(pricelist)//2
                print("market:{},price:{}".format(market, pricelist[mid]))
            else:
                idx1 = len(pricelist)//2
                idx2 = len(pricelist)//2 -1
                median = (pricelist[idx1] + pricelist[idx2])/2
                print("market:{},price:{}".format(market, median))

if __name__=='__main__':
    arr = [
        ('San Francisco', 100),
        ('San Francisco', 200),
        ('San Francisco', 150),
        ('New York', 250),
        ('New York', 110),
        ('New York', 190),
        ('Boston', 160),
        ('Boston', 100),
        ('Boston', 90)
    ]
    s = Solution()
    (s.median_price(arr))