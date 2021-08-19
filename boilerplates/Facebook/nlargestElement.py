# Given a ´dictionary, print the key for nth highest value present in the dict.
# If there are more than 1 record present for nth highest value then sort the key and
# print the first one.


input = {'a':1,'b':2,'c':3,'d':4,'e':3,'f':4, 'g':5}

from heapq import heapify, heappop, heappush, nlargest
from collections import defaultdict

heap = []
inverseDict = defaultdict(list)
for k, v in input.items():
    if v not in inverseDict:
        heappush(heap, v)
        inverseDict[v].append(k)

nthLargestVal = nlargest(10, heap)[-1]

print('val: {}, key: {} '.format(nthLargestVal, sorted(inverseDict[nthLargestVal])[0]))