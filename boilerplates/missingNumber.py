class Solution:
    def missingNumber(self, nums):
        nums.sort()
        result = []
        for i in range(1, len(nums)):
            flag = True
            if nums[i] - nums[i-1] > 1:
                temp = nums[i]
                while flag:
                    result.append(temp - 1)
                    temp -= 1
                    if temp - nums[i-1] > 1:
                        continue
                    else:
                        flag = False
        return result

if __name__=='__main__':
    s = Solution()
    assert s.missingNumber([3,0,1]) == [2]
    assert s.missingNumber([2,4,7,8,9,15]) == [3, 6, 5, 14, 13, 12, 11, 10]